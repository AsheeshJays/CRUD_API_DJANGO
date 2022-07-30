from django.shortcuts import render
from .serializers import EmployeeSerializer
from mainApp.models import Employee
from rest_framework import viewsets

class EmployeeModelViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
