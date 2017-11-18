from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# The categories model within which are tagged posts
class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)


    # To effect informal rendering of fields, eg : from "<Model Object>" 
    # to "Title":
    def __str__(self):
        return self.title

    # Change the name in Admin from categorys to categories
    class Meta:
        verbose_name_plural = "categories"

     #Define the slug for URLs
    def slug(self):
        return slugify(self.title)


# The main posts model
class Post(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=500, default = True)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    category = models.ManyToManyField('Category')
    author = models.ForeignKey(User, default=True)
    slug = models.SlugField(max_length=100, unique=True)
    

    def __str__(self):
        return self.title

    def slug(self):
          return slugify(self.title)



# # The comments model for user to post comments
class Comment(models.Model):
    #FK = many-to-one - many comments can relate to one post
    post = models.ForeignKey(Post)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

