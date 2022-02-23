from django.shortcuts import render
from blog.models import *
from django.core.paginator import Paginator

def base(request):
    context = { 
    	'date': 2020
    }
    return context

def index(request):
    categorys = Category.objects.all()
    posts = Post.objects.select_related('category', 'author').all().order_by('-time_registered')

    new_posts = posts[:2]

    paginator = Paginator(posts, 1)

    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)

    context = {
        'categorys': categorys,
        'posts': posts,
        'new_posts': new_posts,
        'page_posts': page_posts
    }

    return render(request, "home/index.html", context)