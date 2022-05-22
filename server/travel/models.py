from django.db import models

class Travel(models.Model):
    country = models.CharField(max_length=100)
    continent = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    message = models.CharField(max_length=500, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

