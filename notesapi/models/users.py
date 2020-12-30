from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    password = models.CharField(max_length=20)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.mobile}"
