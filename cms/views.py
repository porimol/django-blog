from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from cms.models import Post, Category

# Index view
def index(request):
    return HttpResponse("Hi")

# home view
def home(request):
    blog_posts = Post.objects.order_by('-pub_date')[:10]
    categories = Category.objects.all()
    template = loader.get_template('frontend/home.html')
    context = {
        'blog_posts': blog_posts,
        'categories': categories,
    }

    return HttpResponse(template.render(context, request))

# Get the single post details
def single_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    categories = Category.objects.all()
    template = loader.get_template('frontend/single.html')
    context = {
        'post': post,
        'categories': categories,
    }
    return HttpResponse(template.render(context, request))

def post_by_category(request, category_id):
    blog_posts = Post.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    template = loader.get_template('frontend/home.html')

    context = {
        'blog_posts': blog_posts,
        'categories': categories,
    }

    return HttpResponse(template.render(context, request))
