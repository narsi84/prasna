from django.contrib.postgres.fields import IntegerRangeField
from django.contrib.postgres.validators import RangeMinValueValidator
from django.db import models

from django.db.models import CASCADE
from django.utils.safestring import mark_safe
from model_utils.models import TimeStampedModel


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(default='apple.jpg')

    def image_tag(self):
        return mark_safe('<img width=50px height=50px src="{}" />'.format(self.image.url))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.name


class QuizItem(TimeStampedModel):
    LOW = (0, 'Low')
    MEDIUM = (1, 'Medium')
    HIGH = (2, 'High')
    LEVELS = set([LOW, MEDIUM, HIGH])

    category = models.ForeignKey(Category, on_delete=CASCADE)
    age = IntegerRangeField(validators=[RangeMinValueValidator(1)])
    difficulty = models.IntegerField(choices=LEVELS, default=0)

    q_text = models.TextField(null=False)
    q_image = models.ImageField(null=True, blank=True)

    a_text = models.TextField(null=False)
    a_image = models.ImageField(null=True, blank=True)
    a_media_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.q_text} => {self.a_text}'

    def q_image_tag(self):
        if self.q_image:
            return mark_safe('<img width=50px height=50px src="{}" />'.format(self.q_image.url))
        return ''

    def a_image_tag(self):
        if self.a_image:
            return mark_safe('<img width=50px height=50px src="{}" />'.format(self.a_image.url))
        return ''

    q_image_tag.short_description = 'Q Image'
    a_image_tag.short_description = 'A Image'
