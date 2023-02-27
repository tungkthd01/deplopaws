from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models.base import Model
from django.forms import widgets
from django.forms.models import ModelForm
from main import models
from main.models import User,Post


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required = True)

    class Meta:
        model = User
        fields =["username","email","password1","password2"]

    def save(self, commit = True):
        user = super(NewUserForm,self).save(commit=False)
        user.email = self.cleaned_data.get('email')
        if commit:
            user.save()
        return user

class PostFormList(forms.ModelForm):
    #owner = forms.(User)
    class Meta:
        model = Post
        fields = ["title","decription","file","keyencrytion","owner"]
        keyencrytion_choices =(('RSA', 'RSA'),
			('ECC', 'ECC'),
            ('DSA', 'DSA'),)
        widgets ={
            "keyencrytion": forms.Select(choices=keyencrytion_choices,attrs={'class':'form-control'}),
            # "owner" : forms.HiddenInput()
        }
    
   