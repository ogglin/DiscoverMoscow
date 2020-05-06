from collections import namedtuple

from django import template
import re

from django.db import connection

from ..models import AllTag, BlogIndexPage

register = template.Library()


def GetAllTag():
    cursor = connection.cursor()
    cursor.execute(
        'SELECT tt.id, bc.order_num, bc.parent_id_id, bc."order", tt.name, bc.name title, bc.color FROM taggit_tag tt LEFT JOIN blog_coloredtag bc ON tt.id = bc.tag_id GROUP BY tt.id ORDER BY bc.order_num')
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    rows = [nt_result(*row) for row in cursor.fetchall()]
    return rows

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

@register.simple_tag
def a_tags():
    all_tags = GetAllTag()
    return all_tags

@register.simple_tag
def c_tags():
    all_tags = GetAllTag()
    primary = []
    for tag in all_tags:
        if tag.order == '0':
            primary.append(tag.id)
    card_tags = dict.fromkeys(primary)
    for el in card_tags:
        arr = []
        for tag in all_tags:
            if tag.order != '0' and el == tag.parent_id_id:
                arr.append(tag.id)
        card_tags[el] = arr
    return card_tags