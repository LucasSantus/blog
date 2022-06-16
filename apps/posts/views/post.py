from django.shortcuts import render, redirect
from posts.models import Post
from posts.forms import PostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

@login_required
def register_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.save()
            messages.success(request, f"Postagem registrada com sucesso!")
            return redirect('/')
    context = {
        "form": form,
        "action": "Registrar",
    }

    return render(request, 'posts/post/register_post.html', context)

@login_required
def change_post(request, slug_post):
    post = Post.objects.select_related('author').get(slug = slug_post)
    form = PostForm(instance = post)
    if request.method == "POST":
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            messages.success(request, f"Postagem modificada com sucesso!")
            return redirect('detail_post', slug_post = post.slug)

    context = {
        "form": form,
        "action": "Modificar",
    }

    return render(request, 'posts/post/register_post.html', context)

@login_required
def detail_post(request, slug_post):
    post = Post.objects.select_related('author').get(slug = slug_post)
    context = {
        "post": post,
    }
    return render(request, 'posts/post/detail_post.html', context)

@login_required
def delete_post(request, slug_post):
    Post.objects.get(slug = slug_post).delete()
    messages.success(request, f"Postagem deletada com sucesso!")
    return redirect("/")

@login_required
def user_posts(request, id_user):
    posts = Post.objects.select_related('author').filter(author__id = id_user).order_by('-create_at')

    first_post = posts.first()

    paginator = Paginator(posts, 8)
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)

    context = {
        'page_posts': page_posts,
        'author': first_post.author
    }

    return render(request, 'posts/post/user_posts.html', context)
