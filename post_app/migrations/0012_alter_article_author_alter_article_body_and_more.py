# Generated by Django 5.1.4 on 2025-03-09 11:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0011_alter_article_author_alter_article_body'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(help_text='ENTER VALID VALUE HERE', max_length=70, unique=True),
        ),
    ]
