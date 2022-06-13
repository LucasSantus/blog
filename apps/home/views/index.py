from django.shortcuts import render
from posts.models import *
from django.core.paginator import Paginator

def index(request):
    posts = Post.objects.select_related('author').all().order_by('-create_at')[2:]

    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)

    print("\n\n\n\n\n\n\n\n\n\n\n\n")
    print(page_posts)

    context = {
        'posts': posts,
        'page_posts': page_posts
    }

    return render(request, "home/index.html", context)