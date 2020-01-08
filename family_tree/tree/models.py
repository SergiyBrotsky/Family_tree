from django.db import models

# Create your models here.
class Form(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)