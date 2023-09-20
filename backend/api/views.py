from blogapp.models import Article
from .serializer import ArticleSerializer, UserSerializer, LoginSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework import generics, authentication, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from django.contrib.sessions.models import Session


# Authentication Views

# Register
class RegisterUser(APIView):
	def post(self, request):
		serializer = UserSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data)


# Login

# views.py


class LoginUser(APIView):
	def post(self, request):
		if request.user.is_authenticated:
			return Response({'message': 'You are already logged in.'}, status=status.HTTP_200_OK)

		if request.method == 'POST':
			username = request.data.get('username')
			password = request.data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				request.session.set_expiry(0)
				request.session.save()
				return Response({'message': 'Login successful.'}, status=status.HTTP_200_OK)
			else:
				return Response({'message': 'Login failed. Please check your credentials.'},
								status=status.HTTP_401_UNAUTHORIZED)


# Logout
class LogoutUser(APIView):
	authentication_classes = [SessionAuthentication,]

	def post(self, request):
		logout(request)
		return Response({'message': 'Logout successful.'}, status=status.HTTP_200_OK)


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
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	authentication_classes = [authentication.SessionAuthentication, ]
	# permission_classes = [permissions.IsAuthenticated,]


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
