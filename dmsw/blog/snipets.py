from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet


# @register_snippet
# class BlogCategory(models.Model):
#     name = models.CharField(max_length=255)
#     icon = models.ForeignKey(
#         'wagtailimages.Image', null=True, blank=True,
#         on_delete=models.SET_NULL, related_name='+'
#     )
#
#     panels = [
#         FieldPanel('name'),
#         ImageChooserPanel('icon'),
#     ]
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name_plural = 'категории'


@register_snippet
class MediaKit(models.Model):
    mediakit = models.FileField(verbose_name='mediakit', null=True, blank=True)

    panels = [
        FieldPanel('mediakit'),
    ]

    class Meta:
        verbose_name_plural = 'Медиакит'


@register_snippet
class AddToProject(models.Model):
    email = models.CharField(max_length=255, null=True, blank=True)
    # subject = models.CharField(max_length=255, null=True, blank=True, verbose_name='Тема письма')

    panels = [
        FieldPanel('email'),
        # FieldPanel('subject'),
    ]

    def __str__(self):
        return self.email

    def get_all(self):
        return self.email, self.subject

    class Meta:
        verbose_name_plural = 'Присоединиться к проекту'
