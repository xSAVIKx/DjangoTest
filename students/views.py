from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


class StudentCreateView(CreateView):
    pass


class StudentUpdateView(UpdateView):
    pass


class StudentDeleteView(DeleteView):
    pass


class StudentDetailView(DetailView):
    pass


class GroupCreateView(CreateView):
    pass


class GroupUpdateView(UpdateView):
    pass


class GroupDeleteView(DeleteView):
    pass


class GroupDetailView(DetailView):
    pass