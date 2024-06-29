# Generated by Django 5.0.4 on 2024-06-22 23:01

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_article_image_alter_article_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('event_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата проведения')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение')),
                ('is_past_event', models.BooleanField(default=False, verbose_name='Прошедшее мероприятие')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery/', verbose_name='Изображение')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='news.event')),
            ],
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]