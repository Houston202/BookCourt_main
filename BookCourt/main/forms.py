from .models import Users
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, URLInput

class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ["company_name", "mobile_phone", "email", "url", "adres",
                  "name_of_major", "password"]

        widgets = {
            "company_name": TextInput(attrs={
                'class': 'input',
                'placeholder': 'Название компании',
                'required': 'required'
            }),
            "mobile_phone": TextInput(attrs={
                'class': 'input',
                'placeholder': 'Телефон',
                'required': 'required'
            }),
            "email": EmailInput(attrs={
                'class': 'input',
                'placeholder': 'Email',
                'required': 'required'
            }),
            "url": URLInput(attrs={
                'class': 'input',
                'placeholder': 'Ссылка на сайт',
                'required': 'required'
            }),
            "adres": TextInput(attrs={
                'class': 'input',
                'placeholder': 'Адрес',
                'required': 'required'
            }),
            "name_of_major": TextInput(attrs={
                'class': 'input',
                'placeholder': 'Представитель (ФИО)',
                'required': 'required'
            }),
            "password": PasswordInput(attrs={
                'class': 'input',
                'placeholder': 'Пароль',
                'required': 'required'
            })
        }















