from django.db import models
from django.utils import timezone

class Event(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    description = models.TextField('Описание', blank=True)
    event_date = models.DateTimeField('Дата публикации', default=timezone.now)
    image = models.ImageField('Изображение', upload_to='images/', blank=True, null=True)
    is_past_event = models.BooleanField('На страницу "Памятники"', default=False)
    list_title = models.CharField(max_length=255, default='Название списка', blank=True)

    def __str__(self):
        return self.title

class Gallery(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField('Изображение', upload_to='gallery/')
    description = models.CharField('Описание', max_length=200, blank=True)

    def __str__(self):
        return f"Фото для {self.event.title}"

class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField('Автор', max_length=100)
    text = models.TextField('Комментарий')
    created_date = models.DateTimeField('Дата создания', default=timezone.now)
    approved = models.BooleanField('Одобрено', default=False)
    image = models.ImageField('Изображение', upload_to='comments/', blank=True, null=True)

    def approve(self):
        self.approved = True
        self.save()

    def __str__(self):
        return f"Комментарий от {self.author} на {self.event.title}"

class Paragraph(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='paragraphs')
    content = models.TextField('Содержание',  blank=True)

    def __str__(self):
        return f"Абзац для {self.event.title}"

class ListItem(models.Model):
    event = models.ForeignKey(Event, related_name='list_items', on_delete=models.CASCADE)
    title = models.CharField('Заголовок', max_length=200)
    description = models.TextField('Описание', blank=True)
    image = models.ImageField('Изображение', upload_to='list_item_images/', null=True, blank=True)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField('Имя', max_length=100)
    email = models.EmailField('Электронная почта')
    message = models.TextField('Сообщение')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.created_at}'

class Announcement(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    description = models.TextField('Описание')
    created_at = models.DateTimeField('Дата создания', default=timezone.now)

    def __str__(self):
        return self.title

class AnnouncementImage(models.Model):
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField('Изображение', upload_to='announcement_images/')
    
    def __str__(self):
        return f"Изображение для {self.announcement.title}"
