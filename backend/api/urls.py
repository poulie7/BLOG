from django.urls import path
from .views import ArticleView, UserView, CreateArticle

urlpatterns = [
	path('', ArticleView.as_view(), name='article_view'),
	path('post/', UserView.as_view(), name='user_view'),
	path('edit/', CreateArticle.as_view(), name='createArticle_view'),

]
