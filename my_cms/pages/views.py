from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


class DashboardPageView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"
    redirect_field_name = 'login'