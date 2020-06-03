from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register, ModelAdminGroup)
from .models import Tags, TagColors, TagsEN, TagColorsEN, BlogPage, BlogPageEN, TypedPage, TypedPageEN
from slider.models import Photo, PhotoEN
from dop_slider.models import Sliders, SlidersEN


class BlogPageInline(ModelAdmin):
    model = BlogPage
    menu_label = 'Статьи'
    menu_icon = 'folder-open-inverse'
    menu_order = 10

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(locale='ru')


class BlogPageInlineEN(ModelAdmin):
    model = BlogPageEN
    menu_label = 'Articles'
    menu_icon = 'folder-open-inverse'
    menu_order = 10

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(locale='en')


class SlidersInline(ModelAdmin):
    model = Sliders
    menu_label = 'Доп. слайдер'
    menu_icon = 'folder-open-inverse'
    menu_order = 100
    list_display = ('title', 'image', 'order_num', 'ontop', 'draft')
    list_filter = ('title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(locale='ru')


class SlidersInlineEN(ModelAdmin):
    model = SlidersEN
    menu_label = 'Functional slider'
    menu_icon = 'folder-open-inverse'
    menu_order = 100
    list_display = ('title', 'image', 'order_num', 'ontop', 'draft')
    list_filter = ('title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(locale='en')


class PhotoInline(ModelAdmin):
    model = Photo
    menu_label = 'Слайдер слева'
    menu_icon = 'folder-open-inverse'
    menu_order = 50
    list_display = ('title', 'image', 'order_num', 'ontop', 'draft')
    list_filter = ('title',)
    index_template_name = 'modeladmin/index.html'
    inspect_template_name = 'modeladmin/inspect.html'

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(locale='ru')


class PhotoInlineEN(ModelAdmin):
    model = PhotoEN
    menu_label = 'Slider on the left'
    menu_icon = 'folder-open-inverse'
    menu_order = 50
    list_display = ('title', 'image', 'order_num', 'ontop', 'draft')
    list_filter = ('title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(locale='en')


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

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(locale='en')


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

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(locale='en')


class TypedPageInline(ModelAdmin):
    model = TypedPage
    menu_label = 'Статичные страницы'
    menu_icon = 'folder-open-inverse'
    menu_order = 200

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(locale='ru')


class TypedPageInlineEN(ModelAdmin):
    model = TypedPageEN
    menu_label = 'Static pages'
    menu_icon = 'folder-open-inverse'
    menu_order = 200

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(locale='en')


class LocaleRU(ModelAdminGroup):
    menu_label = 'Русский'
    menu_icon = 'folder-open-inverse'
    menu_order = 200
    items = (BlogPageInline, PageTagInline, PageTagColors, PhotoInline, SlidersInline, TypedPageInline)


class LocaleEN(ModelAdminGroup):
    menu_label = 'English'
    menu_icon = 'folder-open-inverse'
    menu_order = 200
    items = (BlogPageInlineEN, PageTagInlineEN, PageTagColorsEN, PhotoInlineEN, SlidersInlineEN, TypedPageInlineEN)


modeladmin_register(LocaleRU)
modeladmin_register(LocaleEN)
