from django.shortcuts import render, redirect
from .models import Post, Category, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

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

@login_required
def home(request):
    return render(request, 'registration/home.html')

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
