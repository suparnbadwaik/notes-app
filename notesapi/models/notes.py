from notesapi.models.users import User
from django.db import models


class Note(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="note")
    heading = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    isdeleted = models.BooleanField(default=False)
    createddate = models.DateTimeField(auto_now_add=True)
    modifieddate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.heading} - {self.modifieddate}"
