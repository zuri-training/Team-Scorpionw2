from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Website
from django.urls import reverse_lazy
from django.views.generic import (
	ListView,
	DetailView,
    TemplateView,
	)
from django.views.generic.edit import(
	CreateView,
	UpdateView,
	DeleteView,
	)

from .forms import WebsiteForm


class TemplatePageView(TemplateView):
    template_name = "templates.html"


class PortfolioPageView(DetailView):
    template_name = "portfolio.html"
    model = Website



# class MyakocityPageView(TemplateView):
#     template_name = "myakocity.html"


class WebsiteSuccessView(LoginRequiredMixin, TemplateView):
	template_name = 'create_success.html'


class WebsiteCreateView(LoginRequiredMixin, CreateView):
	model = Website
	form_class = WebsiteForm
	template_name = 'create.html'
	success_url = reverse_lazy('create_success')

	def form_valid(self,form):
            form.instance.user = self.request.user
            return super().form_valid(form)

# 	fields = [
#         "user",
#         "title",
#         "occupation",
#         "about_me",
#         "skill1",
#         "skill2",
#         "skill3",
#         "skill4",
#         "fb",
#         "twitter",
#         ]

