from django import forms 
from .models import Avaliacao, Curso, Modulo
from django.contrib.auth import get_user_model

class CursoForm(forms.Form, forms.ModelForm):
    professores = forms.ModelMultipleChoiceField(get_user_model().objects.filter(user_type=2))
    nome = forms.CharField(max_length=100)
    class Meta:
        model = Curso

        fields = [
            "nome", "professores"
        ]
    # class Meta:
    #     model = Curso

    #     fields = [
    #         "nome",
    #         "professores"
    #         ]
        