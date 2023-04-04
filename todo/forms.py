from django import forms
from todo.models import Tasks
from django.contrib.auth.models import User
class TaskForm(forms.ModelForm):
    class Meta:
        model=Tasks
        fields=['task_name','user']

        widgets={
            'task_name':forms.TextInput(attrs={"class":"form-control"}),
            "user":forms.TextInput(attrs={"class":"form-control"})
        }

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password']

        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'})
        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control"}))
    