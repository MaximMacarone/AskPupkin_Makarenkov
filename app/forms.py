from django import forms
from django.contrib.auth.models import User

from app.models import Profile, Question, Answer


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        return self.cleaned_data['username'].lower().strip()

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean(self):
        data = super().clean()
        print(data)
        if data['password'] != data['password_confirm']:
            raise forms.ValidationError('Passwords do not match')

        return data


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = {'nickname', 'avatar'}


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {'email', 'username'}


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = {'nickname', 'avatar'}

class AskQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = {'title', 'body', 'tags'}

class AddAnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = {'content'}