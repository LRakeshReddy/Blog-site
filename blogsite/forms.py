from django import forms

class BlogForm(forms.Form):
    blog_text = forms.CharField(max_length=200, widget=forms.Textarea)

class RegisterForm(forms.Form):
    username = forms.CharField(label="Username", max_length=50)
    first_name=forms.CharField(label="First Name", max_length=50)
    last_name=forms.CharField(label="Last Name", max_length=50)
    email=forms.CharField(label="Email", max_length=100)
    password1=forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirm Password", max_length=50, widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=50)
    password=forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput)

