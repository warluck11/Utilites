from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class services(models.Model):
    
    type=(("Book Gas", "Book Gas"), ("New Connection", "New Connection"), 
          ("Locate Distributor", "Locate Distributor"), ("Request Customer Service", "Request Customer Service"))
    
    stats = (("Submitting", "Submitting"), ("Assessing", "Assessing"), ("Fulfilling", "Fulfilling"),
             ("Closed", "Closed"))
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50)
    mobile =  models.BigIntegerField()
    service = models.CharField(max_length = 50, choices=type)
    status = models.CharField(max_length = 50, choices=stats, default="Submitting")
    file = models.ImageField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
   
  