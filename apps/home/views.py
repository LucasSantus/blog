from django.shortcuts import render
from django.utils import timezone
from cadastro.models import Post

def index(request):
    list_posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date') 
    
    context = {
        "list_posts": list_posts
    }
    
    return render(request, 'cadastro/index.html', context)