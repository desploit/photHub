from django.shortcuts import render, redirect
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

def Add_post(request):
    if request.method == 'POST':
        Post_title = request.POST.get("post_title")
        Post_description = request.POST.get("post_description")
        post_image = request.POST.get("Image_url")
        post_category = request.POST.get("Post_category")
        post_user = request.POST.get("Post_user")

        # create_post = [
        #     user == post_user,
        #     category == post_category,
        #     Title == Post_title,
        #     description == Post_description,
        #     post_image == post_image
        # ]
        Post.objects.create(
            user = post_user,
            category = post_category,
            Title = Post_title,
            description = Post_description,
            Post_image = post_image
        )
        return redirect("post created success")

    categories = Post_category.objects.all()
    users = User.objects.all()
    context = {
        "users":users,
        "categories":categories,
    }
    return render(request, "pages/add_post.html", context)

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