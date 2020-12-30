from django.urls import path
from notesapi.views.notes import (
    NoteDetailAPIView, NoteListCreateAPIView)

urlpatterns = [
    path("", NoteListCreateAPIView.as_view(), name="note_list_create"),
    path("<int:pk>", NoteDetailAPIView.as_view(), name="note_detail_modify")
]
