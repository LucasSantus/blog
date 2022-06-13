from django import forms
from posts.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "subtitle", "description"]

        error_messages = {
            "title":{
                "required": "O título é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um título válido!",
            },
            "subtitle":{
                "required": "O sub título é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um sub título válido!",
            },
            "description":{
                "required": "A descrição é obrigatória para realizar o registro!",
                "invalid": "Por favor, insira uma descrição válida!",
            },
        }
