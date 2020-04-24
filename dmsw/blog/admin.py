from django.contrib import admin

# Register your models here.
from .models import BlogPageTag

@admin.register(BlogPageTag)
class BlogPageTag(admin.ModelAdmin):
    pass