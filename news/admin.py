from django.contrib import admin
from .models import Event, Gallery, Comment, Paragraph, ListItem, ContactMessage, Announcement, AnnouncementImage

class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 1

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'event', 'approved', 'created_date')
    list_filter = ('approved', 'created_date')
    search_fields = ('author', 'text')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
    approve_comments.short_description = 'Одобрить выбранные комментарии'

class ParagraphInline(admin.StackedInline):
    model = Paragraph
    extra = 1

class ListItemInline(admin.TabularInline):
    model = ListItem
    extra = 1
    
class AnnouncementImageInline(admin.TabularInline):
    model = AnnouncementImage
    extra = 1

class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ('title', 'event_date')
    search_fields = ('title', 'event_date')
    ordering = ('-event_date',)
    inlines = [ListItemInline, GalleryInline, ParagraphInline]

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'message']

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
    inlines = [AnnouncementImageInline]

admin.site.register(Event, EventAdmin)
admin.site.register(Comment, CommentAdmin)
