
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from django import forms
from .models import *

class AddRecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Recipes
        fields = '__all__' # говорит какие поля нужноотобразить в форме (указали все поля, кроме тех что заполняются автоматически)

    # title = forms.CharField(max_length=255, label='Заголовок')
    # slug = forms.SlugField(max_length=255, label='url_slug')
    # content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Содержание')
    # is_published = forms.BooleanField(label='Публикация', required=False, initial=True)
    # category = forms.ModelChoiceField(queryset=Categories.objects.all(), label='Категория', empty_label='Категория не выбрана')


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class': 'form-input'}))