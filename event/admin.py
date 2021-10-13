from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'start_time', 'end_time', 'location', 'is_active')
    list_display_links = ('title',)
    search_fields = ('title',)