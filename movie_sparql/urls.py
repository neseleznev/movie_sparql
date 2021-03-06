"""movie_sparql URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from web.views import SearchView, MovieView, ContributorView, GenreView

urlpatterns = [
    url(r'^$', SearchView.as_view(), name='search'),
    url(r'^movie/(?P<name>.+)$', MovieView.as_view(), name='movie-detail'),
    url(r'^contributor/(?P<name>.+)$', ContributorView.as_view(), name='contributor-detail'),
    url(r'^genre/(?P<name>.+)$', GenreView.as_view(), name='genre-detail'),
    url(r'^admin/', admin.site.urls),
]
