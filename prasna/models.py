from django.contrib.postgres.fields import IntegerRangeField, ArrayField
from django.contrib.postgres.validators import RangeMinValueValidator
from django.db import models

from django.db.models import CASCADE, SET_NULL
from django.utils.safestring import mark_safe
from model_utils.models import TimeStampedModel


class Media(TimeStampedModel):
    IMAGE = 'Image'
    AUDIO = 'Audio'
    VIDEO = 'Video'
    TYPES = (IMAGE, AUDIO, VIDEO)

    file = models.FileField(blank=False, null=False)
    type = models.CharField(max_length=50, null=False, blank=False, choices=zip(TYPES, TYPES))
    name = models.CharField(max_length=100, null=False, blank=False)

    def tag(self):
        self.get_media_tag(self)

    def __str__(self):
        return f'{self.name} - {self.type}'

    @classmethod
    def get_media_tag(cls, field):
        if field:
            if field.type == Media.IMAGE:
                return mark_safe(f'<img width=100 height=50 src="{field.file.url}" />')
            elif field.type == Media.AUDIO:
                return mark_safe(
                    f'<audio style="width: 10em" controls> <source src="{field.file.url}" type="audio/mpeg"> <audio/>'
                )
            else:
                return mark_safe(
                    f'<video width="100" height="100" controls> <source src="{field.file.url}" '
                    f'type="audio/mpeg"> '
                    f'<video/>'
                )
        return ''


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(null=False, blank=False)

    def image_tag(self):
        return mark_safe(f'<img width=50px height=50px src="{self.image.url}" />')

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class QuizItem(TimeStampedModel):
    LOW = (0, 'Low')
    MEDIUM = (1, 'Medium')
    HIGH = (2, 'High')
    LEVELS = set([LOW, MEDIUM, HIGH])

    category = models.ForeignKey(Category, on_delete=CASCADE)
    age = IntegerRangeField(validators=[RangeMinValueValidator(1)])
    difficulty = models.IntegerField(choices=LEVELS, default=0)

    q_text = models.TextField(null=False)
    q_image = models.ForeignKey(Media, null=True, blank=True, on_delete=SET_NULL,
                                related_name='q_images')
    q_audio = models.ForeignKey(Media, null=True, blank=True, on_delete=SET_NULL,
                                related_name='q_audios')
    q_video = models.ForeignKey(Media, null=True, blank=True, on_delete=SET_NULL,
                                related_name='q_videos')

    a_text = models.TextField(null=False)
    a_image = models.ForeignKey(Media, null=True, blank=True, on_delete=SET_NULL,
                                related_name='a_images')

    tags = ArrayField(models.CharField(max_length=20), size=10, default=list, blank=True)

    def __str__(self):
        return f'{self.q_text} => {self.a_text}'

    def q_image_tag(self):
        return Media.get_media_tag(self.q_image)

    def q_audio_tag(self):
        return Media.get_media_tag(self.q_audio)

    def q_video_tag(self):
        return Media.get_media_tag(self.q_video)

    def a_image_tag(self):
        return Media.get_media_tag(self.a_image)

    def test_url(self):
        return mark_safe(f'<a href="/static/index.html?id={self.id}" target="_blank">Test</a>')

    q_image_tag.short_description = 'Q Image'
    q_video_tag.short_description = 'Q Video'
    q_audio_tag.short_description = 'Q Audio'
    a_image_tag.short_description = 'A Image'
    test_url.short_description = 'Test'

    class Meta:
        verbose_name_plural = 'Quiz items'
