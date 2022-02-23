from django.shortcuts import render, redirect
from blog.models import Post
from blog.forms import PostForm
from django.contrib import messages

def register_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, f"Post registrado com sucesso!")
            return redirect('/')

    context = {
        "form": form,
        "action": "Registrar"
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
            messages.success(request, f"Post modificado com sucesso!")
            return redirect('detail_post', slug = post.slug)

    context = {
        "form": form,
        "action": "Modificar",
    }

    return render(request, 'blog/post/register_post.html', context)

def detail_post(request, slug_post):
    post = Post.objects.get(slug = slug_post)
    context = {
        "post": post,
    }

    return render(request, 'blog/post/detail_post.html', context)

def delete_post(request, slug_post):
    Post.objects.get(slug = slug_post).delete()
    messages.success(request, f"Post deletado com sucesso!")
    return redirect("/")