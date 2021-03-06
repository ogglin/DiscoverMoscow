from django import template
from django.apps import apps
from django.template.loader import get_template

Photo = apps.get_model('slider', 'Photo')

register = template.Library()


# t = get_template('dop_slider/dop_slider.html')

@register.simple_tag()
def get_slides():
    return Photo.objects.all()


@register.inclusion_tag('slider/slider.html')
def show_slides(locale):
    if locale == 'ru':
        return {'slides': Photo.objects.filter(locale=locale)}
    elif locale == 'en':
        return {'slides': Photo.objects.filter(locale=locale)}

# register.inclusion_tag(t)(show_slides)
