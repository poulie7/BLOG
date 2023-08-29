from django.urls import path
from . views import ArticleView, UserView



urlpatterns = [
	path('', ArticleView.as_view(), name='article_view'),
	path('post/', UserView.as_view(), name='user_view'),
]