from django.contrib import admin

from django.db import models
from django.forms import Textarea, NumberInput

from prasna.models import QuizItem, Category, Media


class QuizItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'test_url', 'category', 'difficulty', 'age', 'q_text', 'q_image_tag',
                    'q_audio_tag', 'q_video_tag', 'a_text', 'a_image_tag', 'tags')
    readonly_fields = ('q_image_tag', 'a_image_tag', 'q_audio_tag', 'q_video_tag')
    search_fields = ['a_text', 'q_text', 'tags']
    list_editable = ('category', 'difficulty', 'age', 'q_text', 'a_text', 'tags')
    autocomplete_fields = ['q_image', 'q_audio', 'q_video', 'a_image']
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 40})},
        models.IntegerField: {'widget': NumberInput(attrs={'style': 'width: 5px'})}
    }


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']


class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'tag', 'file')
    readonly_fields = ('tag',)
    search_fields = ['name']
    list_editable = ['name', 'type', 'file']

admin.site.register(Category, CategoryAdmin)
admin.site.register(QuizItem, QuizItemAdmin)
admin.site.register(Media, MediaAdmin)
