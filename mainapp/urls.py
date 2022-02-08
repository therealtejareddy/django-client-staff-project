from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('dashboard', views.dashboardStaff, name="dashboard-staff"),
    path('dashboard-client', views.dashboardClient, name="dashboard-client"),
]