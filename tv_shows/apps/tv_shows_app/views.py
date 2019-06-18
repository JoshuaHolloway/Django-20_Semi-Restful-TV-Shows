from django.shortcuts import render, HttpResponse, redirect
from .models import Shows
# ======================================================================================================================
def index(request):
  return redirect("/shows")
# ======================================================================================================================
def shows(request):
  shows = Shows.objects.all()
  context = {"shows": shows}
  return render(request, "tv_shows_app/index.html", context)
# ======================================================================================================================
def show(request, show_id):
  show = Shows.objects.get(id=show_id)
  context = {"show": show}
  return render(request, "tv_shows_app/show.html", context)
# ======================================================================================================================
def new(request):

  # TODO: DO the query to create a new show

  # TODO: Get the id of the new show

  return render(request, "tv_show_app/show.html")