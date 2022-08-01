import uuid
from xmlrpc.client import DateTime
from django.db import models

# Create your models here.
class Post (models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='img')
    body = models.TextField(
    post_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField()
    
    def _str_(self):
        return self.title
    )
