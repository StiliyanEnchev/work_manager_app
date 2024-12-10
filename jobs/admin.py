from django.contrib import admin

from jobs.models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'salary_per_month', 'owner', 'created_on', 'taken')
    search_fields = ('title', 'description')
    list_filter = ('owner', 'salary_per_month')

