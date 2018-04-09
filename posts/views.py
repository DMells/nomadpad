from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Category

def getPosts(request):
    latest_posts = Post.objects.all().order_by('-pub_date')
    Travelling = Category.objects.filter(name="Travelling")
    childCats = Category.objects.filter(parent=Travelling)
    # childCats = childCats.filter(children__isnull=True)
    context = {
    'latest_posts':latest_posts,
    'childCats':childCats,
    }
    return render(request, 'posts/getPosts.html', context)

def getPost(request, parentSlug, catSlug, postSlug):
    parent = Category.objects.root_nodes()
    childCats = Category.objects.filter(parentSlug=parentSlug)
    childCat = childCats.get(catSlug=catSlug)
    post = Post.objects.get(titleSlug=postSlug)

    context = {
    'parent':parent,
    'childCat':childCat,
    'childCats':childCats,
    'post':post
    }
    return render(request, 'posts/getPost.html', context)

def getCategory(request, parentSlug, catSlug):
    childCats = Category.objects.filter(parentSlug=parentSlug)
    childCat = childCats.get(catSlug=catSlug)
    posts = Post.objects.filter(category=childCat)
    # catA = Category.objects.root_nodes()
    
    context = {
    'childCat':childCat,
    'childCats':childCats,
    'posts':posts
    }
    return render(request, 'categories/getCategory.html', context)

def privacypolicy(request):
    return render(request, 'policies/privacypolicy.html')
 