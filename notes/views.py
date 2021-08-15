from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import DetailView
from .models import Note


class CreateNote(CreateView):
    model=Note
    fields=['title','text_area']
    
    def get_success_url(self):
        reverse_lazy("user_detail", args="{self.request.user.username}")
        return super(CreateNote, self).get_success_url()
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user.userprofile
        obj.save()
        return super( CreateNote, self).form_valid(form)


class UpdateNote(UpdateView):
    model=Note
    fields=['title','text_area']
    
    def dispatch(self, request, *args, **kwargs,):
        if self.request.user.is_authenticated:
            return super(UpdateNote, Note).dispatch(request, *args, **kwargs)
        else:
            return HttpResponse("<h3>not authenticated</h3>")
    
    def get_success_url(self):
        reverse_lazy("user_detail", args="{self.request.user.username}")
        return super(UpdateNote, self).get_success_url()
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user.userprofile
        obj.save()
        return super( UpdateNote, self).form_valid(form)
    
