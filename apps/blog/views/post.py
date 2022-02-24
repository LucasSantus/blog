from django.shortcuts import render, redirect
from blog.models import Category, Post
from blog.forms import PostForm
from django.contrib import messages

def register_post(request, slug_category):
    category = Category.objects.get(slug = slug_category)
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.category = category
            post.save()
            messages.success(request, f"Postagem registrado com sucesso!")
            return redirect('/')

    context = {
        "form": form,
        "action": "Registrar",
        "category": category
    }

    return render(request, 'blog/post/register_post.html', context)

def modify_post(request, slug_post):
    post = Post.objects.get(slug = slug_post)
    form = PostForm(instance = post)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.save()
            messages.success(request, f"Postagem modificado com sucesso!")
            return redirect('detail_post', slug = post.slug)

    context = {
        "form": form,
        "action": "Modificar",
    }

    return render(request, 'blog/post/register_post.html', context)

def detail_post(request, slug_post):
    post = Post.objects.select_related('author', 'category').get(slug = slug_post)
    context = {
        "post": post,
    }

    return render(request, 'blog/post/detail_post.html', context)

def delete_post(request, slug_post):
    Post.objects.get(slug = slug_post).delete()
    messages.success(request, f"Postagem deletado com sucesso!")
    return redirect("/")
