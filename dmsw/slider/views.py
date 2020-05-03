from django.shortcuts import render

# Create your views here.
from .models import Photo

# gallery = Gallery.objects.all()
slides = Photo.objects.all()