from django.urls import path
from .views import (
    TemplatePageView,
)


urlpatterns = [
    path("template/", TemplatePageView.as_view(), name="template"),
]