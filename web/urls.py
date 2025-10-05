from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'web-home'), 
    path('about/',views.about, name='web-about'),
    path('detail/<int:pk>/',views.detail,name='web-detail'),
    path('create/',views.create,name='web-create'),
]