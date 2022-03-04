from django import forms
from django.contrib.auth.models import Group
from .models import *

class UsuarioForm(forms.ModelForm):
    confirm_password = forms.CharField(
        max_length = 60, 
        required = True, 
        label = "Confirmação",
        error_messages = {
            "required": "A confirmação de senha é obrigatória para realizar o registro!",
            "invalid": "Por favor, insira uma confirmação de senha válida!",
        },
    )
    
    def save(self, commit=True):
        user = super(UsuarioForm, self).save(commit = False)
        user.set_password(self.cleaned_data['password'])
        user.is_active = True
        user.is_staff = False
        user.is_superuser = False
        if commit:
            user.save()
        return user

    class Meta:
        model = Usuario

        fields = ["name", "last_name", "email", "password", "confirm_password"  ]

        error_messages = {
            "name":{
                "required": "O nome é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um nome válido!",
            },

            "last_name":{
                "required": "O sobrenome é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um sobrenome válido!",
            },
            "email":{
                "required": "O e-mail é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um e-mail válido!",
            },
            "password":{
                "required": "A senha é obrigatória para realizar o registro!",
                "invalid": "Por favor, insira uma senha válida!",
            },
        }

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ["name", "last_name", "email", "description" ]

        error_messages = {
            "name":{
                "required": "O nome é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um nome válido!",
            },
            "last_name":{
                "required": "O sobrenome é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um sobrenome válido!",
            },
            "email":{
                "required": "O e-mail é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um e-mail válido!",
            },
            "cell_phone":{
                "required": "O celular é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um celular válido!",
            },
        }