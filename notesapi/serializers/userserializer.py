from datetime import datetime
from django.utils.timesince import timesince
from django.db.models import fields
from rest_framework import serializers
from notesapi.models.notes import Note
from notesapi.models.users import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #exclude = ("id",)
        fields = "__all__"
