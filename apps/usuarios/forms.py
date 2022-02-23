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
        # fields = ["nome", "sobrenome", "email", "data_nascimento", "celular",  "password", "confirm_password"]

        fields = ("__all__")

        # error_messages = {
        #     "email":{
        #         "required": "O e-mail é obrigatório para realizar o registro!",
        #         "invalid": "Por favor, insira um e-mail válido!",
        #     },
        #     "nome":{
        #         "required": "O nome é obrigatório para realizar o registro!",
        #         "invalid": "Por favor, insira um nome válido!",
        #     },

        #     "sobrenome":{
        #         "required": "O sobrenome é obrigatório para realizar o registro!",
        #         "invalid": "Por favor, insira um sobrenome válido!",
        #     },
            
        #     "celular":{
        #         "required": "O celular é obrigatório para realizar o registro!",
        #         "invalid": "Por favor, insira um celular válido!",
        #     },
            
        #     "password":{
        #         "required": "A senha é obrigatória para realizar o registro!",
        #         "invalid": "Por favor, insira uma senha válida!",
        #     },
            
        #     "data_nascimento":{
        #         "invalid": "Por favor, insira um formato válido de data de nascimento (DD/MM/AAAA)!",
        #     },
        # }