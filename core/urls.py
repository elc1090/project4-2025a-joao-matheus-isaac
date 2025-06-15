from django.urls import path
from .views import home, custom_logout

urlpatterns = [
    path('',        home,         name='home'),
    path('logout/', custom_logout, name='logout'),
]
