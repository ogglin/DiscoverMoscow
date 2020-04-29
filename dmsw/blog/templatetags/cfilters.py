from django import template

register = template.Library()


@register.filter
def clear_url(value):
    return value.replace("/", "")
