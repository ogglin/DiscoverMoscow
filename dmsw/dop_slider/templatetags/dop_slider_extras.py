from django import template
from django.apps import apps
from django.template.loader import get_template
Sliders = apps.get_model('dop_slider', 'Sliders')

register = template.Library()
#t = get_template('dop_slider/dop_slider.html')

@register.simple_tag()
def get_dop_slides():
    return Sliders.objects.all()

@register.inclusion_tag('dop_slider/dop_slider.html')
def show_dop_slides():
    return {'dop_slider': Sliders.objects.all()}

#register.inclusion_tag(t)(show_slides)