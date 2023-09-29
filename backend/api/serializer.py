from blogapp.models import Article
from rest_framework import serializers
from django.contrib.auth.models import User
from django.utils.html import strip_tags
from django.contrib.auth import authenticate

class ArticleSerializer(serializers.ModelSerializer):
	content_plain_text = serializers.CharField(source='content', read_only=True)
	class Meta:
		model = Article
		fields = '__all__'
		# fields= ['article_header', 'article', 'article_categorie']

	def to_representation(self, instance):
		representation = super(ArticleSerializer, self).to_representation(instance)
		representation['article'] = strip_tags(representation['article'])
		return representation

# Serializer to Get User Details using Django Token Authentication
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'first_name', 'last_name', 'email','username', 'password']
	# 	extra_kwargs = {
	# 		'password': {'write_only': True}
	# 	}
	#
	# def create(self, validated_data):
	# 	password = validated_data.pop('password', None)
	# 	instance = self.Meta.model(**validated_data)
	# 	if password is not None:
	# 		instance.set_password(password)
	# 	instance.save()
	# 	return instance


class LoginSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField(write_only=True)

	def validate(self, data):
		username = data.get('username')
		password = data.get('password')

		user = authenticate(username=username, password=password)

		if not user:
			raise serializers.ValidationError("Invalid username or password")

		data['user'] = user  # Add the user to validated data
		return data
