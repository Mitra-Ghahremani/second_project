from django.shortcuts import render
from post_app.models import Article
# Create your views here.
def home(request):
    article=Article.objects.all()
    print(article)
    print(Article.category)
    return render(request,"home_app/index.html",context={'articles':article})