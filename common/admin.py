from django.contrib import admin

from common.models import News, Feedback


# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_on', 'is_active')
    list_filter = ('is_active', 'published_on')
    search_fields = ('title', 'content')
    ordering = ('-published_on',)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'created_on')
    list_filter = ('rating', 'created_on')
    search_fields = ('user__username', 'message')
    ordering = ('-created_on',)
