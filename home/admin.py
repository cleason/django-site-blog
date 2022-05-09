from django.contrib import admin
from .models import BlogModel

# Register your models here.

@admin.register(BlogModel)
class AdminBlogModel(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'upload_to')
    prepopulated_fields = {'slug': ('title',), }
