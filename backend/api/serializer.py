
from blogapp.models import Article
from rest_framework import serializers
from django.contrib.auth.models import User




class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article
		fields = '__all__'


#Serializer to Get User Details using Django Token Authentication
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'first_name', 'last_name', 'username', 'password']
		extra_kwargs = {
			'password': {'write_only': True}
		}

	def create(self, validated_data):
		password = validated_data.pop('password', None)
		instance = self.Meta.model(**validated_data)
		if password is not None:
			instance.set_password(password)
		instance.save()
		return instance

class LoginSerializer(serializers.ModelSerializer):
     class Meta:
         model=User
         fields=('email','password')

# #Serializer to Register User
# class RegisterSerializer(serializers.ModelSerializer):
#   email = serializers.EmailField(
#     required=True,
#     validators=[UniqueValidator(queryset=User.objects.all())]
#   )
#   password = serializers.CharField(
#     write_only=True, required=True, validators=[validate_password])
#   password2 = serializers.CharField(write_only=True, required=True)
#   class Meta:
#     model = User
#     fields = ('username', 'password', 'password2',
#          'email', 'first_name', 'last_name')
#     extra_kwargs = {
#       'first_name': {'required': True},
#       'last_name': {'required': True}
#     }
#   def validate(self, attrs):
#     if attrs['password'] != attrs['password2']:
#       raise serializers.ValidationError(
#         {"password": "Password fields didn't match."})
#     return attrs
#   def create(self, validated_data):
#     user = User.objects.create(
#       username=validated_data['username'],
#       email=validated_data['email'],
#       first_name=validated_data['first_name'],
#       last_name=validated_data['last_name']
#     )
#     user.set_password(validated_data['password'])
#     user.save()
#     return user