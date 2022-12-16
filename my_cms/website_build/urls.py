from django.urls import path
from .views import (
    TemplatePageView,
    WebsiteCreateView,
    WebsiteSuccessView,
)


urlpatterns = [
    path("template/", TemplatePageView.as_view(), name="template"),
    path('create', WebsiteCreateView.as_view(), name='create'),
    path('create_success', WebsiteSuccessView.as_view(), name='create_success'),
]