from django.contrib import admin
from .models import Record

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'first_name', 'last_name', 'email', 'phone', 'city')
    list_filter = ('created_at',)
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('-created_at',)
