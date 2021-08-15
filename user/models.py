from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.urls import reverse


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    
    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"username": self.user.user.username})
    