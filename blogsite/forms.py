from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User, auth
from django.core.exceptions import ValidationError
from django.contrib import messages

class BlogForm(forms.Form):
    blog_text = forms.CharField(max_length=200, widget=forms.Textarea)

class RegisterForm(forms.Form):
    username = forms.CharField(label="Username", max_length=50)
    first_name=forms.CharField(label="First Name", max_length=50)
    last_name=forms.CharField(label="Last Name", max_length=50)
    email=forms.CharField(label="Email", max_length=100)
    password1=forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirm Password", max_length=50, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        if cleaned_data.get('password1') == cleaned_data.get('password2'):
            if User.objects.filter(username=cleaned_data.get('username')).exists():
                raise ValidationError("username taken")
            elif User.objects.filter(email=cleaned_data.get('email')).exists():
                raise ValidationError("email taken")
        else:
            raise ValidationError("passowrds not matching")
        return cleaned_data

    def save(self):
        cleaned_data = self.clean()
        print(cleaned_data)
        user = User.objects.create_user(username=cleaned_data['username'], password=cleaned_data['password1'], email=cleaned_data['email'], first_name=cleaned_data['first_name'], last_name=cleaned_data['last_name'])
        user.save()


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=50)
    password=forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput)
