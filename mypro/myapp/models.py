from django.db import models

# Create your models here.
class rec(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    message=models.CharField(max_length=100)
    def __str__(self):
        return self.name