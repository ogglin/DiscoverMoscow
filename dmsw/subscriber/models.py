from django.db import models

# Create your models here.
from django import forms


class SubscribeForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField(max_length=120)
