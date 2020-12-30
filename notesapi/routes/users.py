from django.urls import path
from notesapi.views.users import (UserCreateListAPIView)

urlpatterns = [
    path("", UserCreateListAPIView.as_view(), name="user_list")
]
