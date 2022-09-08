from django.shortcuts import render
from .models import Post
from django.views import generic

# Create your views here.

class BlogView(generic.DetailView): # pass the data get from the model and pass them to templates
    model = Post
    template_name = 'blog.html'

class AboutView(generic.TemplateView): # you only need to render a template without getting data from the model
    template_name: str = 'about.html'

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-date_created')
    template_name = 'index.html'