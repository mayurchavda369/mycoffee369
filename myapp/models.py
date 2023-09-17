from django.db import models

# Create your models here.
class User(models.Model):

    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    mob=models.CharField(max_length=12)
    password=models.CharField(max_length=100)
    propic=models.FileField(upload_to="user_profile/",default="anonymous.jpg")

    def __str__(self):
        return self.name

