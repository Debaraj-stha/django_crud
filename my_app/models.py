from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=120)
    email=models.EmailField(max_length=122)
    password=models.CharField(max_length=120)
    def __str__(self):
        return self.name
class myUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    profile_picture = models.FileField(upload_to="image/",max_length=200,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Post(models.Model):
     name = models.CharField(max_length=100)
     email = models.CharField(max_length=100)
     password = models.CharField(max_length=100)
     image=models.FileField(upload_to="image/",max_length=200,null=True)
class multipleImage(models.Model):
    images=models.ImageField(upload_to="multiple_image/",max_length=250,null=True)
