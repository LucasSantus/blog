from django import forms
from blog.models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']

        error_messages = {
            "title":{
                "required": "O título é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um título válido!",
            },
        }