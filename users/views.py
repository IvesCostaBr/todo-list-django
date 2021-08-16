from django.shortcuts import render
from django.views import View
from .models import User



class UserDetail(View):
    def get(self, request, *args, **kwargs):
        if User.objects.filter(user__username=kwargs['username']).exists():
            user_detail = User.objects.get(user__username=kwargs['username'])
        return render(request,"user/user_detail.html",{"user":user_detail})
