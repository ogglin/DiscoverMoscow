from django.db import models

from wagtail.core.models import Page
from django.http import HttpResponseRedirect
from django.urls import reverse


class HomePage(Page):
    # def get_context(self, request):
    #     context = super(HomePage, self).get_context(request)
    #     context['blogs'] = self.blogs()
    #     return context
    def serve(self, request):
        print(request.META['HTTP_HOST'], 'home')
        #Redirect to blog index page
        return HttpResponseRedirect('/blog/')
    # def get_context(self, request):
    #     # Update context to include only published posts, ordered by reverse-chron
    #     context = super().get_context(request)
    #     blogpages = self.get_children().live().order_by('-first_published_at')
    #     context['blogpages'] = blogpages
    #     return context
