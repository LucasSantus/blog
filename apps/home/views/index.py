from django.shortcuts import render
from posts.models import *
from django.core.paginator import Paginator

def index(request):
    posts = Post.objects.select_related('author').all().order_by('-create_at')

    paginator = Paginator(posts, 8)
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)

    context = {
        'page_posts': page_posts
    }

    return render(request, "home/index.html", context)