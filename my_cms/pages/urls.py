from django.urls import path
from .views import HomePageView, DashboardPageView


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("dashboard/", DashboardPageView.as_view(), name="dashboard")
]