from django import forms
from .models import Post, Comment

class CommentForm(forms.ModelForm):
	title = forms.CharField(max_length=200,help_text='Enter a comment headline.')
	body = forms.CharField(max_length=200)
	likes=forms.IntegerField(widget=forms.HiddenInput(),initial=0)
	views=forms.IntegerField(widget=forms.HiddenInput(),initial=0)

# An inline class to provide additional information on the form.
	class Meta:
# provide association between the ModelForm and a model.
		model = Comment
		fields=('title', 'body',)
		exclude = ('author', 'pub_date', )
