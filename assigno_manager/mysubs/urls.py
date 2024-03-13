from django.urls import path
from . import views

# router = routers.DefaultRouter()
# router.register(r'submissions', SubmissionViewset)

urlpatterns = [
        path('coursework/<int:unit_id>/', views.coursework),
        path('assignments/', views.assignments),
        path('assignment/<int:unit_id>/<int:work_id>/', views.assignment),
        path('submissions/<int:unit_id>/', views.submissions),
        path('units/', views.units),
        path('notifications/<int:unit_id>/', views.get_notifications),
        path('submit-assignment/', views.submit_assignment),
        path('add-to-calendar/', views.add_to_calendar),
        path('grades/<int:unit_id>/', views.grades),
        path('stats/', views.stats)
        ]