from blogapp.models import Article
from .serializer import ArticleSerializer, UserSerializer, LoginSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from rest_framework import generics, authentication, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from rest_framework import status


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
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)



# Logout
class LogoutUser(APIView):
	def post(self, request):
		response = Response()
		response.delete_cookie('jwt')


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
# permission_classes = [IsAuthenticated]


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
