from django.views.generic import ListView, CreateView
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

# to list all te available template 
class LitsAvailableTemplates(ListView):
    model = Post
    template_name = "available_templates.html"


# to create a new template 
class CreateTemplate(CreateView):
    fields = ["title", "body", ]
    model = Post
    template_name = "create_template.html"
    success_url = ""

def templates_page(request):
    """ Function to render the templates page """
    return render(request, 'cmsapp/templates.html')

def product_page(request):
    """ Function to render the product page """
    return render(request, 'cmsapp/404.html')

def hire_an_expert_page(request):
    """ Function to render the hire an expert page """
    return render(request, 'cmsapp/404.html')

def resource_page(request):
    """ Function to render the resource page """
    return render(request, 'cmsapp/resourcepage.html')