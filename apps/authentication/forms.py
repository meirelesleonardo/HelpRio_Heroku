# -*- encoding: utf-8 -*-
"""
HelpRio 2022 - meirelesleonardo.ti@gmail.com
"""

from curses.ascii import NUL
from django import forms
from users.forms import UserCreationForm
from users.models import User
from apps.instituicao.models import Instituicao


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Usuário",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Senha",
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Novo usuário",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "E-mail",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Senha",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirma Senha",
                "class": "form-control"
            }
         ))
    Instituicao = forms.ModelChoiceField(queryset=Instituicao.objects.all(), widget=forms.HiddenInput()) #widget=forms.HiddenInput(), disabled=True
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        
        