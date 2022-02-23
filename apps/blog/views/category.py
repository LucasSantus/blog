from django.shortcuts import render, redirect
from blog.models import Category
from blog.forms import CategoryForm
from django.contrib import messages

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
            return redirect('detail_category', slug = category.slug)

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

    return redirect("/")