# Generated by Django 5.0.4 on 2024-06-27 21:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0017_announcement'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnouncementImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='announcement_images/', verbose_name='Изображение')),
                ('announcement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='news.announcement')),
            ],
        ),
    ]
