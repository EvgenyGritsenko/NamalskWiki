# Generated by Django 4.0 on 2022-01-30 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Описание')),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='Опубликована')),
            ],
            options={
                'verbose_name': 'Статься',
                'verbose_name_plural': 'Статьи',
                'ordering': ['-published'],
            },
        ),
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='ContactWithAuthorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, verbose_name='Email для обратой связи')),
                ('message', models.TextField(verbose_name='Сообщение автору')),
            ],
            options={
                'verbose_name': 'Связь с автором',
                'verbose_name_plural': 'Связь с автором',
            },
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick', models.CharField(max_length=50, verbose_name='Ник')),
                ('comment', models.CharField(max_length=300, verbose_name='Комментарий')),
                ('article', models.ForeignKey(default=-1, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.articlemodel', verbose_name='Статья')),
            ],
            options={
                'verbose_name': 'Коментарий',
                'verbose_name_plural': 'Коментарии',
            },
        ),
        migrations.AddField(
            model_name='articlemodel',
            name='category',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.PROTECT, to='articles.categorymodel'),
        ),
    ]