from django.urls import path
from .views import (
    TemplatePageView,
    WebsiteCreateView,
    WebsiteSuccessView,
    PortfolioPageView,
)


urlpatterns = [
    path("template/", TemplatePageView.as_view(), name="template"),
    path("portfolio/<int:pk>/", PortfolioPageView.as_view(), name='portfolio'),
    path('create', WebsiteCreateView.as_view(), name='create'),
    path('create_success', WebsiteSuccessView.as_view(), name='create_success'),
]