from django.db import models


class Smartphones(models.Model):
    price = models.FloatField()
    img_url = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    ram = models.IntegerField()
    memory = models.IntegerField()
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
