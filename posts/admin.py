from django.contrib import admin

from .models import Post, Category, Comment, Profile

# class PostAdmin(admin.ModelAdmin):
# 	prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Profile)
# admin.site.register(Post, PostAdmin)