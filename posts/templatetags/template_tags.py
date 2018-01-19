from django import template
from posts.models import Category

register = template.Library()

# Here we are registering a new template to {% load %} at the top of the base
# template. This allows us to have parameterised tags, which allow us to
# highlight in bold which category we are looking at when visiting its page.
# This comes into effect in the getcatlist template, under the 'if c == selected_cat' bit.
@register.inclusion_tag('categories/getCatList.html')
def get_category_list(cat=None):
	return {'cats':Category.objects.all(),
			'selected_cat': cat}

