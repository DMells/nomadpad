from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, unique=True)
    # To effect informal rendering of fields, eg : from "<Model Object>" 
    # to "Title":
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "categories"

    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

class Post(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=500, default=True)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    category = models.ManyToManyField('Category')
    author = models.ForeignKey(User, default=True)
    slug = models.SlugField(blank=True, unique=True)
   
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    author = models.ForeignKey(User, default=True)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    slug = models.SlugField(unique=True, default='')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.user)
   
    # itinerary = models.ForeignKey(itinerary) - potential to link user 
    # profiles to a world map - where are my users travelling now? etc,