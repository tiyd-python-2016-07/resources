from django.db import models


class Ability(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    power_level = models.IntegerField()
