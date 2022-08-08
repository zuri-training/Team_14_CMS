import uuid
from django.db import models
from accounts.models import User
from datetime import datetime

# Create your models here.
class Post (models.Model):
    # Represents the title of the posts 
    title = models.CharField(max_length=500)

    # images to upload
    image = models.ImageField(upload_to='img')

    # body of the posts
    body = models.TextField()

    # id for identifying the posts 
    post_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    # creation date
    created_at = models.DateTimeField(auto_now_add=True,)

    # modified date
    modified_at = models.DateTimeField(auto_now=True,)

    # slug field 
    slug = models.SlugField()
    
    # associating a post to a user
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    # to upload images 
    photo = models.ImageField(upload_to='Picture_Images', default='image.jpg')

    def __str__(self):
        return self.title



    
