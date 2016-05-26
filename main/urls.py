from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'aftermath', views.aftermath, name="aftermath"),
    url(r'leaderboard', views.leaderboard, name="leaderboard"),
]
