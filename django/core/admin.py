from django.contrib import admin
from django.http import HttpRequest
from typing import Any
from core.models import Tag, Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'number_views','created_at')

    def get_readonly_fields(self, request: HttpRequest, obj: Any | None) -> list[str]:
          return [ 'author', 'created_at', 'number_views'] if not obj else [
            'author', 'created_at', 'number_views']

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        return super().save_model(request, obj, form, change)

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
