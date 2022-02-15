from django.shortcuts import render

# Create your views here.
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from employeeApp.serializers import EmployeeSerializer
from employeeApp.models import Employee


# views for testing purpose

class TestClassView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class TestClassCreateView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# views for devlopment purpose


class ListEmployeeAPIView(ListAPIView):
    queryset = Employee.objects.all().order_by('name')
    serializer_class = EmployeeSerializer


class ListEmployeeAPIViewDetails(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class CreateEmployeeAPIView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class UpdateEmployeeAPIView(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DeleteEmployeeAPIView(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
