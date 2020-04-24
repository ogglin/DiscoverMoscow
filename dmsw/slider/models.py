from django.db import models

# Create your models here.
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.core.models import Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.models import ClusterableModel


# class Gallery(ClusterableModel):
#     name = models.CharField(max_length=128)
#     panels = [
#         InlinePanel('photo')
#     ]
#
#     class Meta:
#         verbose_name = 'Слайдер'
#         verbose_name_plural = 'Слайдеры'

class Photo(models.Model):
    #gallery = ParentalKey(Gallery, on_delete=models.CASCADE, related_name='photo')
    title = models.CharField(max_length=128, null=True, blank=True)
    subtitle = models.CharField(blank=True, max_length=250)
    link = models.CharField(blank=False, max_length=255)
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    panels = [
        FieldPanel('title'),
        FieldPanel('subtitle'),
        ImageChooserPanel('image'),
        FieldPanel('link'),
    ]

    class Meta:
        verbose_name = 'Изображение слайдера'
        verbose_name_plural = 'Изображения слайдера'
