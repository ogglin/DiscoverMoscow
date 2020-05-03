from django.shortcuts import render

# Create your views here.
from .models import Photo

dop_slides = Photo.objects.all()