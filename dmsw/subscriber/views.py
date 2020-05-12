from django.shortcuts import render
from django.views.generic import FormView
# Create your views here.

from .models import SubscribeForm


class SubscribeFormView(FormView):
    form_class = SubscribeForm
    template_name = 'ajax.html'
    success_url = '/form-success/'