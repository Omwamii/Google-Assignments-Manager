from django.urls import path, include
from rest_framework import routers
from . import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register()
urlpatterns = [
        path('admin/', admin.site.urls),
        path('api/', include(router.urls))
        ]
