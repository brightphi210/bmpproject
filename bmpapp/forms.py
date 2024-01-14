
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class CustomerForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('first_name', 'username', 'email', 'password1')
        
        # def __init__(self, *args, **kwargs ):
        #     super(CustomerForm, self).__init__(*args, **kwargs)
        #     self.fields['first_name'].widget.attrs.update({'class':'form-control'})
        #     self.fields['username'].widget.attrs.update({'class':'form-control'})
        #     self.fields['email'].widget.attrs.update({'class':'form-control'})
        #     self.fields['password1'].widget.attrs.update({'class':'form-control'})
        #     self.fields['password2'].widget.attrs.update({'class':'form-control'})
            
            
# Create a UserUpdateForm to update a username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name']
        firstname= forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter your first name'}))

# Create a ProfileUpdateForm to update image.
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class BlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commments
        fields = ['body']