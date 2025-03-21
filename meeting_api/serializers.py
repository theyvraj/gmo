from rest_framework import serializers

class MeetingSerializer(serializers.Serializer):
    credentials_path = serializers.CharField(required=False)
    attendees = serializers.ListField(child=serializers.EmailField())
    duration = serializers.IntegerField(default=60)
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    work_start = serializers.IntegerField(default=9)
    work_end = serializers.IntegerField(default=17)
    timezone = serializers.CharField(default='UTC')
    summary = serializers.CharField()
    location = serializers.CharField(required=False, allow_blank=True)
    description = serializers.CharField(required=False, allow_blank=True)