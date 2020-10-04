from django.contrib.auth.models import User, Group
from vh_medproc.models import *
from vh_doctor.models import *
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from vh_medproc.serializers import *
from vh_doctor.serializers import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class MedProcViewSet(viewsets.ModelViewSet):
    queryset = MedProc.objects.all()
    serializer_class = MedProcSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer