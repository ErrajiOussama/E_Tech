from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user =models.OneToOneField(User, null=True, on_delete=models.CASCADE)   
