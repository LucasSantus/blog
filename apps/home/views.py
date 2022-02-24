from django.shortcuts import render
from blog.models import *
from django.core.paginator import Paginator
import datetime

def base(request):
    context = { 
    	'year': datetime.datetime.now().year
    }
    return context

def index(request):
    categorys = Category.objects.all()
    posts = Post.objects.select_related('category', 'author').all().order_by('-time_registered')[2:]
    new_posts = Post.objects.select_related('category', 'author').all().order_by('-time_registered')[:2]

    paginator = Paginator(posts, 10)

    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)

    context = {
        'categorys': categorys,
        'posts': posts,
        'new_posts': new_posts,
        'page_posts': page_posts
    }

    return render(request, "home/index.html", context)