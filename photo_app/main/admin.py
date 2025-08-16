from django.contrib import admin
from .models import Country, Gender, User, Post_category, Post

# Register your models here.

all_models = [
    Country, Gender, User, Post_category, Post
]

admin.site.register(all_models)
