from django import forms
from Kilua.models import Setor, Cargo, UserProfile, Chamados, Prioridade
from django.contrib.auth.models import User

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
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField(max_length=10)
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('codigo_tpuser', 'codigo_cargo')

class ChamadosForm(forms.ModelForm):

    comentario = forms.CharField(max_length=120, help_text="Comentario: ")
    desc_problema = forms.CharField(max_length=120, help_text="Descricao do problema: ")

    class Meta:
        model = Prioridade
        fields = ('id_tpproblema', 'comentario', 'desc_problema')