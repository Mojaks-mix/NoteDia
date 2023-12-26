from django.forms import ModelForm
from .models import Room,User,Topic
from django.contrib.auth.forms import UserCreationForm
from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django.forms import ModelForm



class captchaForm(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

class RoomFormMedia(ModelForm):
    class Meta:
        model=Room
        fields = '__all__'
        exclude = ["host", "participants"]


class RoomForm(ModelForm):
    class Meta:
        model=Room
        fields = ['name','description','topic']
        exclude = ["host", "participants"]

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields= ['name','username','email','major','password1','password2'] 



class UserForm(ModelForm):
    class Meta:
        model=User
        fields=['avatar','major','name','username','email','bio', 'topic']
        exclude=['topic']


class TopicForm(ModelForm):
    class Meta:
        model=Topic
        fields=['name','majors']