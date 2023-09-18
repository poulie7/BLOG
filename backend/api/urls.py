from django.urls import path
from .views import CreateArticle, ArticleView, UpdateArticle, DeleteArticle
from .views import RegisterUser, LoginUser, LogoutUser

urlpatterns = [
	path('create/', CreateArticle.as_view(), name='createArticle_view'),
	path('', ArticleView.as_view(), name='article_view'),
	path('update/<int:pk>', UpdateArticle.as_view(), name='update_view'),
	path('delete/<int:pk>', DeleteArticle.as_view(), name='destroy_view'),
	# path('post/', UserView.as_view(), name='user_view'),
	path('register/', RegisterUser.as_view(), name='register_view'),
	path('login/', LoginUser.as_view(), name="login_view"),
	path('logout/', LogoutUser.as_view(), name="logout_view")

]
