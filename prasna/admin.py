from django.contrib import admin

# Register your models here.
from prasna.models import QuizItem, Category


class QuizItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'difficulty', 'age', 'q_text', 'q_image_tag', 'a_text',
                    'a_image_tag')
    readonly_fields = ('q_image_tag', 'a_image_tag')
    search_fields = ['a_text', 'q_text']
    list_editable = ('category', 'difficulty', 'age', 'q_text', 'a_text')


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(QuizItem, QuizItemAdmin)
