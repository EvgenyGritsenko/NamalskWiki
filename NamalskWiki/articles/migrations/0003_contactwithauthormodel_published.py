# Generated by Django 4.0 on 2022-02-18 09:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_commentmodel_options_commentmodel_published_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactwithauthormodel',
            name='published',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Пришло в...'),
            preserve_default=False,
        ),
    ]
