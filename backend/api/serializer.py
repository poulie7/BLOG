from rest_framework import serializers
from blogapp.models import Article, Article_categories
from blogapp.models import User, Post, Post_comment, Tag, Post_meta, Category

class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article
		fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'
class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = '__all__'
