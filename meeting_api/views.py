import os
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .meeting_organizer import MeetingOrganizer
import datetime

class CreateMeetingView(APIView):
    def post(self, request):
        data = request.data

        try:
            organizer = MeetingOrganizer()
            organizer.authenticate()
        except Exception as e:
            return Response({"error": f"Authentication failed: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        try:
            start_date = datetime.datetime.fromisoformat(data['start_date'])
            end_date = datetime.datetime.fromisoformat(data['end_date'])
            duration = (end_date - start_date).total_seconds() / 60  # Duration in minutes
            
            available_slots = organizer.find_free_time(
                attendees=data['attendees'],
                duration_minutes=duration,
                start_date=start_date,
                end_date=end_date + datetime.timedelta(days=7),  # Look for slots up to a week ahead
                work_hours=(data.get('work_start', 9), data.get('work_end', 17)),
                timezone=data.get('timezone', 'UTC')
            )
            
            if not available_slots:
                return Response({"error": "No available time slots found within the next week."}, status=status.HTTP_400_BAD_REQUEST)

            selected_slot = available_slots[0]  # Select the first available slot
            scheduled_start_time = datetime.datetime.fromisoformat(selected_slot['start'])
            scheduled_end_time = datetime.datetime.fromisoformat(selected_slot['end'])
            
            meeting = organizer.create_meeting(
                summary=data['summary'],
                location=data.get('location', ''),
                description=data.get('description', ''),
                start_time=selected_slot['start'],
                end_time=selected_slot['end'],
                attendees=data['attendees'],
                conference_data=True,
                timezone=data.get('timezone', 'UTC')
            )

            response_data = {
                "calendar_link": meeting.get('htmlLink'),
                "google_meet_link": meeting.get('hangoutLink', '')
            }

            if scheduled_start_time > start_date:
                response_data["message"] = f"Time slot not free, meeting scheduled at {scheduled_start_time.strftime('%Y-%m-%d %H:%M:%S')}."
            else:
                response_data["message"] = f"Meeting scheduled at requested time: {scheduled_start_time.strftime('%Y-%m-%d %H:%M:%S')}."

            return Response(response_data)
        except Exception as e:
            return Response({"error": f"Error creating meeting: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)