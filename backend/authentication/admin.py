from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
    "email",
    "phone_no",
    "first_name",
    "last_name",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("phone_no",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("phone_no",)}),)


admin.site.register(CustomUser, CustomUserAdmin)