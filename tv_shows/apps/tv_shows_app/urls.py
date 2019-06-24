from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index),

  # 1. Show table
  url(r'^trips$', views.trips),  # /shows

  # 2. Show row
  url(r'^trips/(?P<trip_id>\d+)$', views.show_trip),  # localhost:8000/shows/<id>

  # 3. New and Add
  url(r'^trips/new$', views.new),  # /trips/new
  url(r'^trips/new/add$', views.add),  # /trips/new/add

  # 4. Edit
  # URL                  Request   Server-Method   return
  # /users/<id>/edit     GET       edit()
  url(r'^trips/(?P<trip_id>\d+)/edit$', views.edit),  # /trips/<id>/edit
  url(r'^trips/(?P<trip_id>\d+)/edit/apply_edit$', views.apply_edit),  # /trips/<id>/edit/apply_edit

  # 5. Delete
  # URL                  Request   Server-Method   return
  # /users/<id>/delete   GET       delete()        redirect to /trips
  url(r'^trips/(?P<trip_id>\d+)/delete$', views.delete)  # /trips/<id>/delete
]