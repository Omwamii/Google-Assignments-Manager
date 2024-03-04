from django.urls import path
from . import views

# router = routers.DefaultRouter()
# router.register(r'submissions', SubmissionViewset)

urlpatterns = [
        path('coursework/', views.coursework),
        path('assignments/', views.assignments),
        path('submission/', views.submission),
        path('units/', views.units),
        path('notifications/', views.get_notifications),
        path('submit-assignment/', views.submit_assignment),
        path('add-to-calendar/', views.add_to_calendar),
        path('grades/', views.grades),
        path('send-private/', views.send_private_message)
        ]