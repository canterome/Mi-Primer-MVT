from django.db import models

class Parientes(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=15)
    age = models.FloatField()
    tipo_de_parentezco = models.CharField(max_length=10, null=True, blank=True)
    is_active = models.BooleanField(default=True)
