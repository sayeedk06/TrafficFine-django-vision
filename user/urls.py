from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views
from . import views

"""
This contains the url patterns that points to the views that are
called by the user
"""
urlpatterns = [
    path('auth/', include('social_django.urls', namespace='social')), #url for fid or oauth registration
    path('logout/', views.user_logout, name='logout'), #url pointing to the logout function in views.py
    path("", views.index, name='index'), #url pointing to the index function in views.py. Which also contains the login functionality
    path("profile/", views.profile, name='profile'), #url pointing to the profile funtion in views.py
]
