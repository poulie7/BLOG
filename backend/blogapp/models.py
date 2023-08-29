from django.db import models


# Create your models here.

class User(models.Model):
	first_name = models.CharField(max_length=50)
	middle_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	mobile = models.CharField(max_length=15)
	email = models.EmailField(max_length=50)
	password_hash = models.CharField(max_length=64)
	registered_at = models.DateTimeField()
	last_login = models.DateTimeField()
	intro = models.CharField(max_length=50)
	profile = models.TextField()


class Post(models.Model):
	author_id = models.ForeignKey('User', on_delete=models.CASCADE)
	title = models.CharField(max_length=75)
	metaTitle = models.CharField(max_length=100)
	slug = models.CharField(max_length=100)
	summary = models.CharField(max_length=50)
	published = models.BooleanField()
	created_at = models.DateTimeField()
	updated_at = models.DateTimeField()
	published_at = models.DateTimeField()
	content = models.TextField()


class Post_comment(models.Model):
	post_id = models.ForeignKey('Post', on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	published = models.BooleanField()
	created_at = models.DateTimeField()
	published_at = models.DateTimeField()
	content = models.TextField()


class Tag(models.Model):
	tag = models.ManyToManyField('Post')
	title = models.CharField(max_length=100)
	meta_title = models.CharField(max_length=100)
	slug = models.CharField(max_length=100)
	content = models.TextField()


class Post_meta(models.Model):
	post_id = models.ForeignKey('Post', on_delete=models.CASCADE)
	key = models.CharField(max_length=50)
	content = models.TextField()


class Category(models.Model):
	post = models.ManyToManyField('Post')
	title = models.CharField(max_length=75)
	meta_title = models.CharField(max_length=100)
	slug = models.CharField(max_length=100)
	content = models.TextField()


class Article_categories(models.Model):
	categorie = models.CharField('Categorie', max_length=200)


class Article(models.Model):
	article_header = models.CharField('Header', max_length=200)
	article = models.TextField('Article')
	article_categorie = models.ForeignKey(Article_categories, on_delete=models.CASCADE)
