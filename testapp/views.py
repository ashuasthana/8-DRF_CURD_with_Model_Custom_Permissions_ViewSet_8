from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from .permissions import SunnyPermission

# Create your views here. In tshi globally apply authentication in Django Rest Framework using the settings.py file directly.


class EmployeeModelViewSetCBV(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    authentication_classes = [TokenAuthentication, ]
    permission_classes = [SunnyPermission, ]
