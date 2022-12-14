from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class TemplatePageView(TemplateView):
    template_name = "templates.html"
