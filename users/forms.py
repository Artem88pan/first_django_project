from django.contrib.auth.models import User
from django import forms

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        help_texts = {
            'username': 'Только буквыб цифры и символы @/./+/-/_',
        }

        verbose_name = {
            'username': 'login',
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('пароли не совпадают')
        return cd['password2']
