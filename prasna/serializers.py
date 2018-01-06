from rest_framework import serializers

from prasna.models import QuizItem, Category, Media


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        exclude = ['created', 'modified']


class QuizItemSerializer(serializers.ModelSerializer):
    category_image = serializers.ImageField(source='category.image', read_only=True)
    q_image = MediaSerializer(read_only=True)
    q_audio = MediaSerializer(read_only=True)
    q_video = MediaSerializer(read_only=True)
    a_image = MediaSerializer(read_only=True)

    class Meta:
        model = QuizItem
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
