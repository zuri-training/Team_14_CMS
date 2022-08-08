from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(
                                                template_name='accounts/login.html',
                                                redirect_authenticated_user=True,
                                                success_url="landingpage"
                                                ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('emailconfirmation/', views.emailconfirmation, name="registerconfirmation")
]