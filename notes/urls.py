from django.urls import path
from .views import (
    CreateNote,
    UpdateNote
)

urlpatterns = [
    path("create_note", CreateNote.as_view(), name="create_note"),
    path("update_note", UpdateNote.as_view(), name="update_note" )
]
