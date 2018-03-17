from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Category, Comment, Profile
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import CommentForm


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

def getPost(request, slug):
    post = Post.objects.get(titleSlug=slug)
    comments = Comment.objects.count()
    context = {
    'post':post,
    'comments':comments
    }
    return render(request, 'posts/getPost.html', context)

def getCategory(request, slug):
    category = Category.objects.get(slug=slug)
    
    context = {
    'category':category,
    
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

def getAuthorPosts(request, slug):
    author_posts = Post.objects.all()
    author_posts = author_posts.filter(authorSlug=slug)
    
    context = {
        'author_posts':author_posts
    }
    return render(request, 'posts/getAuthorPosts.html', context)

def add_comment_to_post(request, slug):
    post = get_object_or_404(Post, titleSlug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('getPost', slug)
    else:
        form = CommentForm()

    return render(request, 'comments/add_comment_to_post.html', {'form':form})

def privacypolicy(request):
    return render(request, 'policies/privacypolicy.html')
