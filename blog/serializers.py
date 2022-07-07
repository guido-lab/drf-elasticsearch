from contextlib import nullcontext
from django.contrib.auth.models import User
from rest_framework import serializers

from blog.models import Article, Category


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    categories = CategorySerializer(many=True)
    confidence_score = serializers.SerializerMethodField('get_confidence_score', read_only=True)

    class Meta:
        model = Article
        fields = (
            'title', 
            'author', 
            'type', 
            'categories', 
            'content', 
            'created_datetime', 
            'updated_datetime',
            'confidence_score',
            )
    
    def get_confidence_score(self, obj):
        """Get confidence score."""
        if obj.meta:
            return obj.meta.score
        else:
            return None