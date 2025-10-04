from django.urls import path
from web import views

urlpatterns = [
    path('', views.home, name = 'web-home'), 
    path('about/',views.about, name='web-about'),
]