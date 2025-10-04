from django.contrib import admin
from django.urls import include , path
from web import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('web.urls')),
    path('register/',include('users.urls')),
    
]
