from django.contrib import admin
from main.models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', )
	readonly_fields = ('created_at', 'updated_at', )
	search_fields = ['title', 'subtitle', 'content', 'created_at', 'updated_at', ]

admin.site.register(Post, PostAdmin)