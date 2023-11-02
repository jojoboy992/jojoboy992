from django import forms
from .models import *


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "avatar"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "User", "body", "image")
        labels = {
            "image": "Upload Image",
            "User": "Select User",
            "body": "Context",
        }


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "User", "body", "image")

        labels = {
            "image": "",
            "User": "Select User",
            "body": "Context",
        }
