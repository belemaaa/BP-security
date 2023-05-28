from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100, on_delete=models.CASCADE)
    password = models.CharField(max_length=30, blank=False)
    email = models.EmailField(max_length=100)
    bio = models.CharField(max_length=400)
    post = models.ImageField()


    def __str__(self):
        return self.username



class UserProfile(models.Model):
    pass



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    imagebox = models.ImageField()
    caption = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)



