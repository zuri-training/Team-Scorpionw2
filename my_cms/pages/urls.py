from django.urls import path
from .views import (
    HomePageView,
    DashboardPageView,
    AboutPageView,
    ContactPageView,
    PricingPageView,
    MyakocityPageView,
)


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("dashboard/", DashboardPageView.as_view(), name="dashboard"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("pricing/", PricingPageView.as_view(), name="pricing"),
    path("myakocity/", MyakocityPageView.as_view(), name="myakocity")
]