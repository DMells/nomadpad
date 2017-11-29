from django.contrib import admin

from .models import Post, Category, Comment, Profile

# This automatically populates the slug field in the admin panel when it is saved.
# Saves me from having to type it in each time.
class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}

class CategoryAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Profile)
admin.site.register(Comment)