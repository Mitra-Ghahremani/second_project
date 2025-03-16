from django.shortcuts import render
from .models import Article
# Create your views here.
def articles(request):
    post=Article.objects.all()
    return render(request,'post_app/post.html',context={'post':post})