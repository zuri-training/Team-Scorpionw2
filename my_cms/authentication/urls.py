from django.urls import path
from .views import SignUpView
from .views import CustomLoginView


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('login/', CustomLoginView.as_view(), name='login'),
]