from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from cms.models import Post

# Index view
def index(request):
    return HttpResponse("Hi")

# home view
def home(request):
    blog_posts = Post.objects.order_by('-pub_date')[:10]
    template = loader.get_template('frontend/home.html')
    context = {
        'blog_posts': blog_posts,
    }
    return HttpResponse(template.render(context, request))

# Get the single post details
def signle_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    template = loader.get_template('frontend/single.html')
    context = {
        'post': post,
    }
    return HttpResponse(template.render(context, request))
