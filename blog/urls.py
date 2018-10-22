from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views

from django.urls import path

from . import views


urlpatterns = [
    path('', views.allblogs, name='home'),
    path('<int:blog_id/>', views.detail, name='detail'),
]