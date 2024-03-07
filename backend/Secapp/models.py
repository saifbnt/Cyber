# Secapp/models.py
from django.db import models

class Site(models.Model):
    url = models.URLField(unique=True)
    scan_result = models.TextField(null=True, blank=True)

    class Meta:
        app_label = 'Secapp'

