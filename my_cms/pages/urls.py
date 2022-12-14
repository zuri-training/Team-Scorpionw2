from django.urls import path
from .views import (
    HomePageView,
    DashboardPageView,
    AboutPageView,
)


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("dashboard/", DashboardPageView.as_view(), name="dashboard"),
    path("about/", AboutPageView.as_view(), name="about"),
]