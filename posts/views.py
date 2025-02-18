from django.views.generic import ListView
from django.http import HttpRequest, HttpResponse
from .models import Post

class PostList(ListView):
    model = Post
    template_name = "post_list.html"

