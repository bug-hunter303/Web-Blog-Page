
from django.contrib import admin
from django.urls import include , path
from users import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('register/',views.register, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name = "login.html"),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = "logout.html"),name='logout'),
    path('profile/',views.profile, name="profile"),
    path('edit-profile/',views.edit_profile,name='edit-profile'),
] 
