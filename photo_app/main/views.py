from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Country, User, Post_category, Gender

# Create your views here.


def Home_page(response):
    posts = Post.objects.all()
    categories = Post_category.objects.all()
    context = {
        "posts":posts,
        "categories":categories
    }
    return render(response, "pages/home.html", context)

def Add_post(response):
    categories = Post_category.objects.all()
    users = User.objects.all()
    context = {
        "users":users,
        "categories":categories,
    }
    return render(response, "pages/add_post.html", context)

def login_page(response):
    return render(response, "pages/login.html")

def register_page(response):
   
    return render(response, "pages/register.html", )

def view_picture(response, pk):
    picture = Post.objects.get(id=pk)
    context = {
        "picture":picture
    }
    return render(response, "pages/picture.html", context)

def admin_page(response):
    return render(response, "pages/admin.html")