from django.contrib import admin

# Register your models here.
from .models import Sliders

@admin.register(Sliders)
class PhotoInline(admin.ModelAdmin):
    pass

