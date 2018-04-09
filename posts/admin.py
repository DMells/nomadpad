from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {
  	"titleSlug": ("title",),
  }

# # to specify which field should be indented in the admin page admin
class CategoryAdmin(MPTTModelAdmin):
     mptt_indent_field = "name"
     prepopulated_fields = { 
     	"catSlug": ("name",), 
		"parentSlug": ("parent",),
     }

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
