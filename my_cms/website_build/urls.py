from django.urls import path
from .views import (
    TemplatePageView,
    WebsiteCreateView,
)


urlpatterns = [
    path("template/", TemplatePageView.as_view(), name="template"),
    path('create', WebsiteCreateView.as_view(), name='create'),
]