from django.contrib import admin
#from  .models import Article
from . import models

admin.site.register(models.Article)
admin.site.register(models.category)


