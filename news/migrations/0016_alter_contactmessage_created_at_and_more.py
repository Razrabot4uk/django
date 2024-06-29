# Generated by Django 5.0.4 on 2024-06-27 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_rename_paragraph1_paragraph'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='message',
            field=models.TextField(verbose_name='Сообщение'),
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='listitem',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='listitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='list_item_images/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='listitem',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='paragraph',
            name='content',
            field=models.TextField(verbose_name='Содержание'),
        ),
    ]