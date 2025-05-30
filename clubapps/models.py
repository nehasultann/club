from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    club = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    image_url = models.URLField(blank=True, null=True)  # Optional image
    activities = models.ManyToManyField(Activity, blank=True)

    def __str__(self):
        return self.full_name
