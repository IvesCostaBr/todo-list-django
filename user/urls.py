from django.urls import path, include
from .views import UserDetail



urlpatterns = [
    path("profile/<str:username>/", UserDetail.as_view(), name="user_detail"),
    path("notes/", include('notes.urls'))
]
