from django import forms
from Kilua.models import Usuario, Setor, Cargo

class SetorForm(forms.ModelForm):
    nome_setor = forms.CharField(max_length=128, help_text="Nome do Setor")
    localidade = forms.CharField(max_length=128, help_text="Localidade")
    telefone = forms.IntegerField(help_text="Telefone:")

    class Meta:
        model = Setor
        #fields = ('nome_setor', 'localidade', 'telefone')

class CargoForm(forms.ModelForm):
    nome_cargo = forms.CharField(max_length=30, help_text="Insira um nome.")
    nivel_cargo = forms.IntegerField(help_text="Informe um nivel de 1-10")

    class Meta:
        model = Cargo


class UserForm(forms.ModelForm):
    nome = forms.CharField(max_length=100, help_text="Nome Completo")
    email = forms.CharField(max_length=50, help_text="Email")
    senha = forms.CharField(max_length=20, help_text="Senha")

    class Meta:
        model = Usuario
        fields = ('nome', 'email', 'senha')

class LoginForm(forms.ModelForm):
    email = forms.CharField(max_length=50, help_text="Email:")
    senha = forms.CharField(max_length=20, help_text="Senha")

    class Meta:
        model = Usuario
        fields=('email', 'senha')