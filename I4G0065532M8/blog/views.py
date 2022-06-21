#from django.shortcuts import render

from django.views.generic import ListView
from .models import Post


# Create your views here.

class PostListView(ListView):
    model = Post 


class PostCreateView(CreateView):
    model = Post 
    fields = ['_all_']
    success_url = reverse_lazy('blog:all')

class PostDetailView(DetailView):
    model = Post 

class PostUpdateView(UpdateView):
    model = Post 
    fields = ['_all_']
    success_url = reverse_lazy('blog:all') 

class PostDeleteView(DeleteView):
    model = Post 
    fields = ['_all_']
    success_url = reverse_lazy('blog:all') 

