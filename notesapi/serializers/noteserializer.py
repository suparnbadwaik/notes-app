from datetime import datetime
from django.utils.timesince import timesince
from django.db.models import fields
from rest_framework import serializers
from notesapi.models.notes import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        #exclude = ("id",)
        fields = "__all__"
