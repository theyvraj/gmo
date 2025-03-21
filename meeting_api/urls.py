from django.urls import path
from .views import CreateMeetingView

urlpatterns = [
    path('create-meeting/', CreateMeetingView.as_view(), name='create_meeting'),
]