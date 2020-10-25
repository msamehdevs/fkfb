from django.db import models

class InfoIn(models.Model):
    username = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username