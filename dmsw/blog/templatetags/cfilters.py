from django import template
import re

register = template.Library()


@register.filter
def clear_url(value):
    return value.replace("/", "")


@register.filter
def clear_image_url(value):
    stv = str(value)
    v = stv.replace(' ', '_')
    rep = str(re.search('[.]\w.*$', stv).group())
    val = '.original' + str(re.search('[.]\w.*$', stv).group())
    v2 = v.replace(rep, val)
    return v2


@register.filter
def clear_val(value):
    return str(value)