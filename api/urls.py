from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views
from . import views
from django.conf import settings
from django.conf.urls.static import static

"""
This contains the url patterns that points to the view that is called
when the user wants to assign a fine.
"""

urlpatterns = [
    path('test/',views.api_views.as_view()),

]
