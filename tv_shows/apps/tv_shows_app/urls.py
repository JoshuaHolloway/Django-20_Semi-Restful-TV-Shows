from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index),

  # 1. Show table
  url(r'^shows$', views.shows),  # /shows

  # 2. Show row
  url(r'^shows/(?P<show_id>\d+)$', views.show),  # localhost:8000/shows/23

  # 3. New and Add
  url(r'^shows/new$', views.new),  # /shows/new
  url(r'^shows/new/add$', views.add),  # /shows/new/add

  # TODO:
  # 4. Edit
  # url(r'^shows/edit$', views.edit),  # /shows/edit

  # 5. Delete
  # URL                  Request   Server-Method   return
  # /users/<id>/delete   GET       delete()        redirect to /shows
  url(r'^shows/(?P<show_id>\d+)/delete$', views.delete)  # /shows/new
]