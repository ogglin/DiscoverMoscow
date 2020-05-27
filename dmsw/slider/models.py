from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class Photo(models.Model):
    # gallery = ParentalKey(Gallery, on_delete=models.CASCADE, related_name='photo')
    text_colors = [
        ('white', 'Белый'),
        ('black', 'Черный'),
    ]
    locales = [
        ('ru', 'ru'),
        ('en', 'en'),
    ]
    locale = models.CharField(max_length=250, verbose_name="Language", choices=locales, default='ru')
    title = models.CharField(max_length=128, null=True, blank=True)
    subtitle = models.CharField(blank=True, max_length=250)
    link = models.CharField(blank=False, max_length=255)
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    text_color = models.CharField(max_length=250, choices=text_colors, default='white',
                                  verbose_name="Цвет текста")
    panels = [
        MultiFieldPanel([
            FieldPanel('title'),
            FieldPanel('subtitle'),
            FieldPanel('text_color'),
            ImageChooserPanel('image'),
            FieldPanel('link'),
        ])
    ]

    class Meta:
        verbose_name = 'Изображение слайдера'
        verbose_name_plural = 'Изображения слайдера'
        ordering = ['-id']


class PhotoEN(Photo):
    locale = 'en'
    list_display = (Photo.title, Photo.link)

    def get_queryset(self, request):
        qs = super(PhotoEN, self).get_queryset(request)
        return qs.filter(locale='en')

    def save(self, *args, **kwargs):
        self.locale = 'en'
        return super().save(*args, **kwargs)
