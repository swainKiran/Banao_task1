from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup, dashboard, profile

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/users/login/'), name='logout'),
    path('profile/', profile, name='profile'),
]
