from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register, ModelAdminGroup)
from .models import Tags, TagColors, TagsEN, TagColorsEN
from slider.models import Photo, PhotoEN
from dop_slider.models import Sliders, SlidersEN


class SlidersInline(ModelAdmin):
    model = Sliders
    menu_label = 'Доп. слайдер'
    menu_icon = 'folder-open-inverse'
    menu_order = 100
    list_display = ('title', 'image')
    list_filter = ('title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(locale='ru')


class SlidersInlineEN(ModelAdmin):
    model = SlidersEN
    menu_label = 'Functional slider'
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


class PhotoInlineEN(ModelAdmin):
    model = PhotoEN
    menu_label = 'Slider on the left'
    menu_icon = 'folder-open-inverse'
    menu_order = 50
    list_display = ('title', 'image')
    list_filter = ('title',)


class PageTagInline(ModelAdmin):
    model = Tags
    menu_label = 'Меню / Теги'
    menu_icon = 'folder-open-inverse'
    menu_order = 150
    list_display = ('id', 'name', 'level', 'parent_id', 'order_num')
    list_filter = ('name',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(locale='ru')


class PageTagInlineEN(ModelAdmin):
    model = TagsEN
    menu_label = 'Menu / Tags'
    menu_icon = 'folder-open-inverse'
    menu_order = 150
    list_display = ('id', 'name', 'level', 'parent_id', 'order_num')
    list_filter = ('name',)


class PageTagColors(ModelAdmin):
    model = TagColors
    menu_label = 'Цвета тегов'
    menu_icon = 'folder-open-inverse'
    menu_order = 200
    list_display = ('color_title', 'color')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(locale='ru')


class PageTagColorsEN(ModelAdmin):
    model = TagColorsEN
    menu_label = 'Tag colors'
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
    items = (PageTagInlineEN, PageTagColorsEN, PhotoInlineEN, SlidersInlineEN)


# class Locales(ModelAdminGroup):
#     menu_label = 'Меню / Теги / Слайдеры'
#     menu_icon = 'folder-open-inverse'
#     menu_order = 200
#     items = (LocaleRU, LocaleEN)


modeladmin_register(LocaleRU)
modeladmin_register(LocaleEN)
