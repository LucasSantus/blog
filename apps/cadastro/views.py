from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import PostForm

def post_new(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('index')
        
    context = {
        "form": form,
    }
    
    return render(request, 'cadastro/post_new.html', context)