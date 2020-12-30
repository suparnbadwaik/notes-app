from django.contrib import admin
from notesapi.models.notes import Note
from notesapi.models.users import User

# Register your models here.
admin.site.register(User)
admin.site.register(Note)
