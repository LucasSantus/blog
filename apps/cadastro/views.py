from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import PostForm

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        
    context = {
        "form": form,
    }
    
    return render(request, 'cadastro/post_edit.html', context)