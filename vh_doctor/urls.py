#urls.py
from django.urls import include, path
from rest_framework import routers
from vh_doctor import views

router = routers.DefaultRouter()
router.register(r'doctor', views.DoctorViewSet, basename='doctor')

urlpatterns = [
    path('', include(router.urls)),
    
    
]