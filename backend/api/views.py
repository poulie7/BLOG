# from rest_framework.decorators import api_view
from rest_framework.response import Response
from blogapp.models import Article, Article_categories
from blogapp.models import User, Post
from .serializer import ArticleSerializer, UserSerializer, PostSerializer
from rest_framework import generics


#Authentication Views

#SignUp

#Login


#Logout

class UserView(generics.RetrieveAPIView):
	queryset = User.objects.all()

	def get(self, request, *args, **kwargs):
		queryset = self.get_queryset()
		serializer = UserSerializer(queryset, many=True)
		return Response(serializer.data)


#CRUD

#Create
class CreateArticle(generics.CreateAPIView):
	# queryset = Article.objects.all()
	serializer_class = ArticleSerializer

#Read
class ArticleView(generics.ListAPIView):
	queryset = Article.objects.all()

	def get(self, request, *args, **kwargs):
		queryset = self.get_queryset()
		serializer = ArticleSerializer(queryset, many=True)
		return Response(serializer.data)
#Update
class UpdateArticle(generics.UpdateAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer


#Delete
class DeleteArticle(generics.DestroyAPIView):
	pass

