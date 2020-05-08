from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register, ModelAdminGroup)
from .models import ColoredTag, TagColors

class PageTagInline(ModelAdmin):
    model = ColoredTag
    menu_label = 'Теги'
    menu_icon = 'folder-open-inverse'
    menu_order = 200
    list_display = ('id', 'order', 'tag', 'parent_id', 'order_num')
    list_filter = ('tag',)


class PageTagColors(ModelAdmin):
    model = TagColors
    menu_label = 'Цвета тегов'
    menu_icon = 'folder-open-inverse'
    menu_order = 201
    list_display = ('color_title', 'color')


modeladmin_register(PageTagInline)
modeladmin_register(PageTagColors)
