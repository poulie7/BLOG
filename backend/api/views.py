from blogapp.models import Article
from .serializer import ArticleSerializer, UserSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics, authentication, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User


# Authentication Views

# Register
# class RegisterUser(APIView):
# 	def post(self, request):
# 		serializer = UserSerializer(data=request.data)
# 		serializer.is_valid(raise_exception=True)
# 		serializer.save()
# 		return Response(serializer.data)


class RegisterView(generics.CreateAPIView):
	serializer_class = UserSerializer

	def post(self, request):
		serializer = UserSerializer(data=request.data)

		if serializer.is_valid():
			first_name = serializer.validated_data.get('first_name')
			last_name = serializer.validated_data.get('last_name')
			email = serializer.validated_data.get('email')
			username = serializer.validated_data.get('username')
			password = serializer.validated_data.get('password')

			user = User.objects.create_user(
				first_name=first_name,
				last_name=last_name,
				email=email,
				username=username,
				password=password
			)
			user.save()

			return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Login

class LoginView(ObtainAuthToken):
	serializer_class = LoginSerializer
	authentication_classes = [TokenAuthentication, ]

	def post(self, request, *args, **kwargs):
		serializer = self.serializer_class(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data['user']
		token, created = Token.objects.get_or_create(user=user)
		return Response({'token': token.key})


# Logout
class LogoutView(APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]

	def post(self, request):
		# Check if the user is authenticated before trying to delete the token.
		if request.user.is_authenticated:
			token = Token.objects.get(user=request.user)
			token.delete()
			return Response(status=status.HTTP_200_OK)
		else:
			# Handle the case where the user is not authenticated.
			return Response(status=status.HTTP_401_UNAUTHORIZED)


# class UserView(generics.RetrieveAPIView):
# 	queryset = User.objects.all()
#
# 	def get(self, request, *args, **kwargs):
# 		queryset = self.get_queryset()
# 		serializer = UserSerializer(queryset, many=True)
# 		return Response(serializer.data)


# CRUD

# Create
class CreateArticle(generics.CreateAPIView):
	authentication_classes = [authentication.TokenAuthentication, ]
	permission_classes = [permissions.IsAuthenticated]
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer


# Read
class ArticleView(generics.ListAPIView):
	queryset = Article.objects.all()

	def get(self, request, *args, **kwargs):
		queryset = self.get_queryset()
		serializer = ArticleSerializer(queryset, many=True)
		return Response(serializer.data)


# Update
class UpdateArticle(generics.RetrieveUpdateAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	lookup_field = 'pk'


# Delete
class DeleteArticle(generics.RetrieveDestroyAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	lookup_field = 'pk'
