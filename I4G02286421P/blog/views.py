from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
class PostListView(ListView):
    model = Post
    
class PostCreateView(CreateView):
    model = Post
    fields = '__all__' #includes all the field of the model
    success_url  = reverse_lazy('blog:all' )#resolving django urls names into url paths

class PostDetailView(DetailView):
    model = Post

class PostUpdateView(UpdateView):
    model = Post
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')

class PostDeleteView(UpdateView):
    model = Post
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')

