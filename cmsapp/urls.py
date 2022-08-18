from django.urls import path
from . import views

app_name = "cmsapp"

urlpatterns = [
    path('', views.landing_page, name="landingpage"),
    path('templates/', views.templates_page, name="templates_page"),
    path('jayn/', views.jayn_page, name="jayn_page"),
    path('clady/', views.clady_page, name="clady_page"),
    path('inyang/', views.inyang_page, name="inyang_page"),
    path('product/', views.product_page, name="product_page"),
    path('resource/', views.resource_page, name="resource_page"),
    path('hire_an_expert/', views.hire_an_expert_page, name="hire_an_expert_page"),
    path('post/', views.index, name='index'),
]