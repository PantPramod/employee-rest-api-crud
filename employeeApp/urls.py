from django.contrib import admin
from django.urls import path
from employeeApp import views


urlpatterns = [
    # for testing
    path("test/<int:pk>/", views.TestClassView.as_view(), name="test"),
    path("test/", views.TestClassCreateView.as_view(), name="test_create"),


    # development mode
    path("", views.ListEmployeeAPIView.as_view(), name="employee_list"),
    path("<int:pk>/", views.ListEmployeeAPIViewDetails.as_view(),
         name="employee_details"),
    path("create/", views.CreateEmployeeAPIView.as_view(), name="employee_create"),
    path("update/<int:pk>/", views.UpdateEmployeeAPIView.as_view(),
         name="update_employee"),
    path("delete/<int:pk>/", views.DeleteEmployeeAPIView.as_view(),
         name="delete_employee"),
]
