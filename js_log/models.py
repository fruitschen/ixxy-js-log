from django.db import models

class Error(models.Model):
    hexdigest = models.CharField(max_length=128)
    first_happened = models.DateTimeField()
    last_happened = models.DateTimeField()
    details = models.TextField()
    number = models.IntegerField()
