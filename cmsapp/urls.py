from django.urls import path
from . import views

app_name = "cmsapp"

urlpatterns = [
    path('', views.landing_page, name="landingpage"),
    path('templates/', views.templates_page, name="templates_page"),
    path('post/', views.index, name='index'),
]