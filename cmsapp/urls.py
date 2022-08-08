from django.urls import path
from . import views

app_name = "cmsapp"

urlpatterns = [
    path('', views.landing_page, name="landingpage"),
    path('post/', views.index, name='index'),
]