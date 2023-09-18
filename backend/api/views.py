from blogapp.models import Article
from .serializer import ArticleSerializer, UserSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from rest_framework import generics, authentication, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login


# Authentication Views

# Register
class RegisterUser(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


# Login

class LoginUser(APIView):
    authentication_classes = [SessionAuthentication]
    def post(self, request):
        content = {
            'username': str(request.user),  # `django.contrib.auth.User` instance.
            'password': str(request.user),  # None
        }



# Logout
class LogoutUser(APIView):
	pass



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
