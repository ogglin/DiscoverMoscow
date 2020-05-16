from collections import namedtuple

from django import template
import re

from django.db import connection

from ..models import Tags

register = template.Library()


@register.simple_tag
def to_project():
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM blog_addtoproject')
    rows = cursor.fetchall()
    row = []
    if len(rows) > 0:
        row = rows[0]
    cursor.close()

    return row


@register.simple_tag
def media_kit():
    cursor = connection.cursor()
    cursor.execute(f'SELECT mediakit FROM blog_mediakit')
    rows = cursor.fetchall()
    row = []
    if len(rows) > 0:
        row = rows[0]
    print(row)
    cursor.close()

    return row


@register.filter
def clear_url(value):
    print(value)
    val = re.search(r'\w+[\/]$', value).group(0)
    print(val)
    return val.replace('/', '')


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


@register.filter
def label_with_classes(value, arg):
    return value(attrs={'class': arg})


@register.simple_tag
def all_tags(lang):
    return Tags.objects.filter(locale=lang)


@register.simple_tag
def a_tags(lang):
    return Tags.objects.filter(locale=lang).order_by('order_num')


@register.simple_tag
def c_tags(lang):
    all_tags = Tags.objects.filter(locale=lang).order_by('order_num')
    primary = []
    for tag in all_tags:
        if tag.level == 0:
            primary.append(tag.id)
    card_tags = dict.fromkeys(primary)
    for el in card_tags:
        arr = []
        for tag in all_tags:
            if tag.level != 0 and el == tag.parent_id_id:
                arr.append(tag.id)
        card_tags[el] = arr
    return card_tags
