from django.shortcuts import render, redirect
from .models import Post, Category, Comment, Profile, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist

def getAllCategories(request):
    categories = Category.objects.all()

    context = {
        'categories':categories
            }

    return render(request, 'categories/getAllCategories.html', context)

def getAllPosts(request):
    latest_posts = Post.objects.all().order_by('-pub_date')
    comments = Comment.objects.all().order_by('-pub_date')
    context = {
    'latest_posts':latest_posts,
    'comments':comments
    }
    return render(request, 'posts/getAllPosts.html', context)


def getPost(request, pk=False):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.count()
    context = {
    'post':post,
    'comments':comments
    }
    return render(request, 'posts/getPost.html', context)

def getCategory(request, pk):
    category = Category.objects.get(pk=pk)
    context = {
    'category':category
    }
    return render(request, 'categories/getCategory.html', context)

def getUserProfile(request):
    profile = Profile.objects.all()

    context = {
    'profile':profile
    }
    return render(request, 'registration/profile.html', context)

# @login_required
# def home(request):
#     return render(request, 'registration/home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def getAuthorPosts(request, author=False):
    latest_posts = Post.objects.all()
    author_posts = latest_posts.filter(author=author)
    context = {
    'latest_posts':latest_posts,
    'author_posts':author_posts
    }
    return render(request, 'posts/getAuthorPosts.html', context)
