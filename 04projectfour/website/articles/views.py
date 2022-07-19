from django.views.generic import ListView, DetailView
from .models import Article
class ArticleListView(ListView):
    model = Article
    template_name = 'home.html'
# Create your views here.
class ArticleDetailsView(DetailView):
    model = Article
    template_name = 'detail.html'
    context_object_name = 'batman'