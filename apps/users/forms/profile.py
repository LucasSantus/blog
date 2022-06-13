from django import forms
from users.models import User


class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["name", "email" ]

        error_messages = {
            "name":{
                "required": "O nome é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um nome válido!",
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
