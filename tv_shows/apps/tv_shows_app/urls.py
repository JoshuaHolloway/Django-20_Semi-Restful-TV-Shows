from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index),

  url(r'^shows$', views.shows), # /shows
  url(r'^shows/new$', views.new),  # /shows/new
  url(r'^shows/new/add$', views.add),  # /shows/new/add

  url(r'^shows/(?P<show_id>\d+)$', views.show) # localhost:8000/shows/23
]