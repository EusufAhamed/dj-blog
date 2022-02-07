from django.shortcuts import render

from post.models import Post
from utils.paginator import pagination

def home(req):
    template = 'home.html'
    post_list = Post.objects.all().order_by('-id')

    data = {}
    data['page_title'] = 'home'

    # pagination post list
    data['posts'] = pagination(req, post_list)
    
    return render(req, template, data)
