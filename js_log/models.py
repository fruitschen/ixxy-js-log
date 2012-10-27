from django.db import models

class Error(models.Model):
    hexdigest = models.CharField(max_length=128)
    first_happened = models.DateTimeField()
    last_happened = models.DateTimeField()
    short_message = models.CharField(max_length=128, blank=True)
    user_agent = models.CharField(max_length=256, blank=True)
    details = models.TextField()
    number = models.IntegerField()
