from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article 
import random

def home_view(request, *args, **kwargs):
    random_id = random.randint(1, 4)
    article_obj = Article.objects.get(id=random_id)
    article_query_set = Article.objects.all()
    context = {
        'object_list' :article_query_set,
        'title' : article_obj.title,
        'content' : article_obj.content,
        'id': article_obj.id,
        'object': article_obj,
    }
    HTML_STRING = render_to_string('home_view.html', context= context)
    return HttpResponse(HTML_STRING)