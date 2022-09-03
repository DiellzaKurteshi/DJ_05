from pdb import post_mortem
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class BlogListView(ListView):  #klasa na duhet shkaku i inheritance, me trashegu Blog prej ListView ose DetailView
    model = Post 
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'