from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index),
  url(r'^shows$', views.shows), # /shows
  url(r'^new$', views.new),  # /new
  url(r'^shows/(?P<show_id>\d+)$', views.show) # localhost:8000/shows/23
]