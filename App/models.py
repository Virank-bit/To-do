from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    srno=models.AutoField(auto_created=True,primary_key=True)
    title = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class feedback(models.Model):
    email=models.EmailField()
    desc=models.TextField()

    def __str__(self):
        return self.email