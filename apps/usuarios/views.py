from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from .forms import *
import datetime

class SignUpView(CreateView):
    template_name = 'usuarios/signup/signup.html'
    form_class = UsuarioForm

def perfil(request):
    usuario = request.user
    form = UsuarioForm(instance = usuario)
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance = usuario)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, "usuarios/profile/perfil.html", context)
