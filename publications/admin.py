from django.contrib import admin
from .models import Publication


@admin.register(Publication)
class Publication(admin.ModelAdmin):
    list_display = ('title', 'author',)
    list_filter = ('author',)
