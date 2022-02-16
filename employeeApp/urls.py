from django.urls import path
from employeeApp import views


urlpatterns = [

    path("emp/<int:pk>/", views.EmpClassView.as_view(), name="test"),
    path("emp/", views.TestClassCreateView.as_view(), name="test_create"),

]
