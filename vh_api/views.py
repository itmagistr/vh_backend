from django.contrib.auth.models import User, Group
from vh_medproc.models import *
from vh_doctor.models import *
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from vh_medproc.serializers import *
from vh_doctor.serializers import *


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']

    def get_queryset(self):
        return User.objects.all().order_by('-date_joined')

class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']
    
    def get_queryset(self):
        return Group.objects.all()


class MedProcViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MedProcSerializer
    http_method_names = ['get']
    
    def get_queryset(self):
        return MedProc.objects.all()


class DoctorViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DoctorSerializer
    http_method_names = ['get']
    
    def get_queryset(self):
        return Doctor.objects.all()
