from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'cmsapp/index.html', context)

def landing_page(request):
    """ Function for the landing page """
    return render(request, 'cmsapp/landingpage.html')