from django.contrib import admin

from .models import Post, Category, Comment, Profile


class CategoryAdmin(admin.ModelAdmin):
# This automatically populates the slug field in the admin panel when it is saved.
# Saves me from having to type it in each time.
  prepopulated_fields = {
  	"categorySlug": ("categoryName",),
  	"parentCatSlug": ("parentCategoryName",),
  }
# https://stackoverflow.com/questions/23574181/how-to-add-information-from-another-model-to-admin-edit-page
# class CategoryInline(admin.TabularInline):
# 	model = Category  


class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {
  	"titleSlug": ("title",), "authorSlug":("author",),
  }
  # inlines = [
  # 	CategoryInline,
  # ]






admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Profile)
admin.site.register(Comment)