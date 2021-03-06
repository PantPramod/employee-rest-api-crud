from django.shortcuts import render

# Create your views here.

from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from employeeApp.serializers import EmployeeSerializer
from employeeApp.models import Employee


class EmpClassView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmpClassCreateView(ListCreateAPIView):
    queryset = Employee.objects.all().order_by('id')
    serializer_class = EmployeeSerializer
