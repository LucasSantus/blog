from django.shortcuts import render
from django.utils import timezone
from blog.models import Post

def base(request):
    context = { 
    	'date': 2020
    }
    return context

def index(request):
    list_posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date') 
    
    context = {
        "list_posts": list_posts
    }
    
    return render(request, 'home/index.html', context)