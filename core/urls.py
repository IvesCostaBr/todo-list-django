from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
from notes.api import viewsets as note_views
from users.api import viewsets as user_views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', user_views.UserViewsets, basename='User')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include('home.urls')),
    path('login/', obtain_jwt_token),
    path('token-verify/', verify_jwt_token),
]
