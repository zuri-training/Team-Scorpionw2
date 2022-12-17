from django.db import models
from django.urls import reverse
from authentication.models import CustomUser as User

# Create your models here.
class Website(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        )
    title = models.CharField(max_length=200)
    occupation = models.CharField(max_length=200)
    about_me = models.TextField()
    skill1 = models.CharField(max_length=100, null=True, blank=True)
    skill2 = models.CharField(max_length=100, null=True, blank=True)
    skill3 = models.CharField(max_length=100, null=True, blank=True)
    skill4 = models.CharField(max_length=100, null=True, blank=True)
    fb = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("portfolio", args=[str(self.id)])