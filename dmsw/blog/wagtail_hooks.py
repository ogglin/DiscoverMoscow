from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register, ModelAdminGroup)
from .models import ColoredTag

class PageTagInline(ModelAdmin):
    model = ColoredTag
    menu_label = 'Теги'
    menu_icon = 'folder-open-inverse'
    menu_order = 200
    list_display = ('id', 'parent_id', 'tag', 'order', 'order_num')
    list_filter = ('tag',)

modeladmin_register(PageTagInline)
