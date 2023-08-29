from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic


from .models import Article
from .models import Article_categories



# Create your views here.
class IndexView(generic.ListView):
	template_name = 'blogapp/index.html'
	context_object_name = 'articles'
	def get_queryset(self):
		return Article.objects.all()




class AboutView(generic.DetailView):
	template_name = 'blogapp/about.html'
class ContactView(generic.DetailView):
	template_name = 'blogapp/contact.html'

class FaqView(generic.DetailView):
	template_name=  'blogapp/faq.html'


class ArticleView(generic.DetailView):
	model = Article
	template_name = 'blogapp/article.html'
	def get_queryset(self):
		return Article.objects.all()


