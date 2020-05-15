from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register, ModelAdminGroup)
from .models import ColoredTag, TagColors
from slider.models import Photo
from dop_slider.models import Sliders


class SlidersInline(ModelAdmin):
    model = Sliders
    menu_label = 'Доп. слайдер'
    menu_icon = 'folder-open-inverse'
    menu_order = 100
    list_display = ('title', 'image')
    list_filter = ('title',)


class PhotoInline(ModelAdmin):
    model = Photo
    menu_label = 'Слайдер слева'
    menu_icon = 'folder-open-inverse'
    menu_order = 50
    list_display = ('title', 'image')
    list_filter = ('title',)


class PageTagInline(ModelAdmin):
    model = ColoredTag
    menu_label = 'Меню / Теги'
    menu_icon = 'folder-open-inverse'
    menu_order = 150
    list_display = ('id', 'order', 'tag', 'parent_id', 'order_num')
    list_filter = ('tag',)


class PageTagColors(ModelAdmin):
    model = TagColors
    menu_label = 'Цвета тегов'
    menu_icon = 'folder-open-inverse'
    menu_order = 200
    list_display = ('color_title', 'color')


class LocaleRU(ModelAdminGroup):
    menu_label = 'Русский'
    menu_icon = 'folder-open-inverse'
    menu_order = 200
    items = (PageTagInline, PageTagColors, PhotoInline, SlidersInline)


class LocaleEN(ModelAdminGroup):
    menu_label = 'English'
    menu_icon = 'folder-open-inverse'
    menu_order = 200
    items = (PageTagColors, PhotoInline, SlidersInline)


# class Locales(ModelAdminGroup):
#     menu_label = 'Меню / Теги / Слайдеры'
#     menu_icon = 'folder-open-inverse'
#     menu_order = 200
#     items = (LocaleRU, LocaleEN)


modeladmin_register(LocaleRU)
modeladmin_register(LocaleEN)
