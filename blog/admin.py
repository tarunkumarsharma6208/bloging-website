from django.contrib import admin
from blog.models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish_date', 'author']
    list_per_page = 5
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title']


