from django.db import models

# Create your models here.

class Country(models.Model):
    country_name = models.CharField(max_length=15, blank=False, null=False)
    country_code = models.CharField(blank=False, null=False)

    def __str__(self):
        return self.country_name

class Post_category(models.Model):
    category_name = models.CharField(max_length=20, blank=False, null=False)
    category_icon = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.category_name

class Gender(models.Model):
    gender_type = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return self.gender_type

class User(models.Model):
    firstname = models.CharField(max_length=50, null=False, blank=False)
    lastname = models.CharField(max_length=50, null=False, blank=False)
    username = models.CharField(max_length=50, null=False, blank=False)
    bio = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=False, blank=False)
    Email_address = models.EmailField(blank=False, null=False)
    gender = models.ForeignKey(Gender, blank=True, null=True, on_delete=models.SET_NULL)
    country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.SET_NULL)
    profile_Image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f"{self.username}, {self.profile_Image}"


class Post(models.Model):
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    category = models.ForeignKey(Post_category, blank=False, null=False, on_delete=models.CASCADE)
    Title = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    Post_image = models.ImageField(blank=True, null=True,)

    def __str__(self):
        return self.Title

