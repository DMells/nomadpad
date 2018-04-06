from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ProcessedImageField
from imagekit.processors import *


class Category(models.Model):
    parentCategoryName = models.ForeignKey('self', blank=True, null=True)
    parentCatSlug = models.SlugField(null=True, blank=True, default="travelling")
    categoryName = models.CharField(max_length=200, null=True)
    categorySlug = models.SlugField(null=True, blank=True)
    # To effect informal rendering of fields, eg : from "<Model Object>"
    # to "Title":
    def __str__(self):
        return self.categoryName
        # # https://djangopy.org/how-to/how-to-implement-categories-in-django/
        # # This changes the django admin section to say Travelling - > Vietnam etc.
        # full_path = [self.categoryName]               
        # k = self.parentCategoryName                          

        # while k is not None:
        #     full_path.append(k.categoryName)
        #     k = k.parentCategoryName

        # return ' -> '.join(full_path[::-1])

    class Meta:
        verbose_name_plural = "categories"

    def save(self, *args, **kwargs):
         self.categorySlug = slugify(self.categoryName)
         self.parentCatSlug = slugify(self.parentCategoryName)
         super(Category, self).save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey('Category', null=True, blank=True)
    summary = models.CharField(max_length=500, default=True)
    body = RichTextUploadingField()
    pub_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, default=True)
    titleSlug = models.SlugField(blank=True)
    authorSlug = models.SlugField(blank=True)
    editedimage = ProcessedImageField(upload_to="primary_images", null=True,
                                processors = [Transpose()],
                                format="JPEG")
    show_in_posts = models.BooleanField(default=True)


    def save(self, *args, **kwargs):
        self.titleSlug = slugify(self.title)
        self.authorSlug = slugify(self.author)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    body = models.CharField(max_length=200)
    author = models.ForeignKey(User, default=True)
    approved_comment = models.BooleanField(default=True)

    def __str__(self):
        self.save()
        return self.title

    def approve(self):
        self.approved_comment = True


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    slug = models.SlugField(unique=True, default='')
    profile_picture = models.ImageField(upload_to='profile_images', blank=True)
# blank = True means the user doesn't have to input to this field if they dont want to.
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.user.username)
    #     super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        # return str(self.user)
        return self.user.username

    # itinerary = models.ForeignKey(itinerary) - potential to link user
    # profiles to a world map - where are my users travelling now? etc