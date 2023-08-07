from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=120)
    email=models.EmailField(max_length=122)
    password=models.CharField(max_length=120)
    def __str__(self):
        return self.name