from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'author_name', 'created_at')
	search_fields = ('title', 'author_name')
	list_display_links = ('title',)
