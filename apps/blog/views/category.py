from django.shortcuts import render, redirect
from blog.models import Category, Post
from blog.forms import CategoryForm
from django.contrib import messages
from django.core.paginator import Paginator

def register_category(request):
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Categoria registrado com sucesso!")
            return redirect('/')

    context = {
        "form": form,
        "action": "Registrar"
    }
    return render(request, 'blog/category/register_category.html', context)

def modify_category(request, slug_category):
    category = Category.objects.get(slug = slug_category)
    form = CategoryForm(instance = category)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance = category)
        if form.is_valid():
            form.save()
            messages.success(request, f"Categoria modificada com sucesso!")
            return redirect('/')
   
    context = {
        "form": form,
        "action": "Modificar",
    }
    return render(request, 'blog/category/register_category.html', context)

def detail_category(request, slug_category):
    category = Category.objects.get(slug = slug_category)

    context = {
        "category": category,
    }
    return render(request, 'blog/category/detail_category.html', context)

def delete_category(request, slug_category):
    Category.objects.get(slug = slug_category).delete()
    messages.success(request, f"Categoria deletada com sucesso!")
    return redirect("/")

def view_posts_category(request, slug_category):
    category = Category.objects.get(slug = slug_category)
    posts = Post.objects.select_related('author', 'category').filter(category__id = category.id)
    
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)

    context = {
        "category": category,
        "posts": posts,
        'page_posts': page_posts
    }
    return render(request, 'blog/category/view_posts_category.html', context)