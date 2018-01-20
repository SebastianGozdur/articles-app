"""aticlesapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path

from articlesapp.views import main, uploadArticle, articlesList, article, articleCard, submitVote

urlpatterns = [
    path('admin/', admin.site.urls),
    url('uploadArticle/', uploadArticle, name="uploadArticle"),
    url(r'^$', articlesList, name = "articles"),
    path('article/<str:articleName>/', article, name = "article"),
    path('articleCard/<str:articleName>/', articleCard, name = "articleCard"),
    path('submitVote/', submitVote, name = 'vote')
]