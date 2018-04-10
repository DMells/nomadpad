from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ProcessedImageField
from imagekit.processors import *
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
    name = models.CharField(max_length = 50, unique = True)
    catSlug = models.SlugField(null=True, blank=True)
    # A TreeForeignKey is just a regular ForeignKey that renders form fields 
    # differently in the admin and a few other places.
    parent = TreeForeignKey('self', null=True, blank=True, 
        related_name='children', db_index=True )
    parentSlug = models.SlugField(null=True, blank=True)

    class MPTTMeta:
        # This indicates the natural ordering of the data in the tree.
        order_insertion_by = ['name']

    # class Meta:
    #     verbose_name_plural = "categories"
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
         self.slug = slugify(self.name)
         self.parentSlug = slugify(self.parent)
         super(Category, self).save(*args, **kwargs)

class Post(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey('Category', null=True, blank=True)
    summary = models.CharField(max_length=500, default=True)
    body = RichTextUploadingField()
    pub_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, default=True)
    titleSlug = models.SlugField(blank=True)
    editedimage = ProcessedImageField(upload_to="primary_images", null=True,
                                processors = [Transpose()],
                                format="JPEG")
    show_in_posts = models.BooleanField(default=True)


    def save(self, *args, **kwargs):
        self.titleSlug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
