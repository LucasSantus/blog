from django.shortcuts import render, redirect
from users.forms import ProfileForm
from django.contrib import messages

def profile(request):
    form = ProfileForm(instance = request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f"Perfil atualizado com sucesso!")
            return redirect('profile')

    context = {
        'form': form,
    }

    return render(request, "users/profile/profile.html", context)