from rest_framework import serializers

from prasna.models import QuizItem, Category


class QuizItemSerializer(serializers.ModelSerializer):
    category_image = serializers.ImageField(source='category.image', read_only=True)
    class Meta:
        model = QuizItem
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'