from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ProcessedImageField
from imagekit.processors import *


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, unique=True)
    # To effect informal rendering of fields, eg : from "<Model Object>" 
    # to "Title":
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "categories"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)
  

class Post(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=500, default=True)
    body = RichTextUploadingField()
    pub_date = models.DateTimeField(default=timezone.now)
    category = models.ManyToManyField('Category')
    author = models.ForeignKey(User, default=True)
    titleSlug = models.SlugField(blank=True)
    authorSlug = models.SlugField(blank=True)
    # mainimage = models.ImageField(upload_to="images", null=True)
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
    # profiles to a world map - where are my users travelling now? etc,