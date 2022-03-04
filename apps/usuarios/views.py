from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages

class SignUpView(CreateView):
    template_name = 'usuarios/signup/signup.html'
    form_class = UsuarioForm

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

    return render(request, "usuarios/profile/profile.html", context)

def description_user(request, slug_user):
    usuario = Usuario.objects.get(slug = slug_user)

    context = {
        'usuario': usuario,
    }

    return render(request, "usuarios/description/description_user.html", context)