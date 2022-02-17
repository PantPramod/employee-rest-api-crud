from django.urls import path
from employeeApp import views


urlpatterns = [

    path("emp/<int:pk>/", views.EmpClassView.as_view(), name="Employee id"),
    path("emp/", views.EmpClassCreateView.as_view(), name="Employee Post"),

]
