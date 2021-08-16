from django.db.models.deletion import CASCADE
from core.settings import STATIC_URL
from django.db import models
from users.models import User
from django.urls import reverse



class Note(models.Model):
    STATUS_NOTE = [
        (0, "in progress"),
        (1, "complete")
    ]
    
    owner = models.ForeignKey(User, on_delete=CASCADE)
    title = models.CharField(max_length=30)
    text_area = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=0, choices=STATUS_NOTE)
    
    def __str__(self):
        return str(self.id) + ' ' + str(self.owner.username)
    
    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"username": self.owner.username})
    
    
