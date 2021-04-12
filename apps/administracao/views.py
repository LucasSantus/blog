from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from cadastro.models import Post
from cadastro.forms import PostForm

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        
    context = {
        "form": form,
        "nome_pagina": "Atualizando Post",
    }
    return render(request, 'administracao/post_edit.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        "post": post,
    }
    return render(request, 'administracao/post_detail.html', context)
