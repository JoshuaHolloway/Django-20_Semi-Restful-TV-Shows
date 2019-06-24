from django.shortcuts import render, HttpResponse, redirect
from .models import Trips
# ======================================================================================================================
def index(request):

  # TODO: Change this to Login Screen
  #  -After login, then redirect to /trips


  return redirect("/trips")
# ======================================================================================================================
def trips(request):
  trips = Trips.objects.all()
  context = {"trips": trips}
  return render(request, "tv_shows_app/index.html", context)
# ======================================================================================================================
def show_trip(request, trip_id):
  trip = Trips.objects.get(id=trip_id)
  context = {"trip": trip}
  return render(request, "tv_shows_app/show.html", context)
# ======================================================================================================================
def get_trip_info(trip_id):
  # Specific show
  trip = Trips.objects.get(id=trip_id)

  # To pass into HTML
  return {"trip": trip}
# ======================================================================================================================
def new(request):
  return render(request, "tv_shows_app/new.html")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def add(request):
  title = request.POST['title']

  # TODO
  # network = request.POST["network"]
  # release_date = request.POST["release_date"]
  # description = request.POST["description"]

  # TODO: Get {network, release_date, description} from form
  trip = Trips.objects.create(title=title)
  return render(request, "tv_shows_app/show.html", get_trip_info(trip.id))
# ======================================================================================================================
def delete(request, trip_id):
  Trips.objects.get(id=trip_id).delete()
  return redirect("/trips")
# ======================================================================================================================
def edit(request, trip_id):
  return render(request, "tv_shows_app/edit.html", get_trip_info(trip_id))
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def apply_edit(request, trip_id):

  trip = Trips.objects.get(id=trip_id)
  title = request.POST['title']
  trip.title = title # TODO

  # TODO
  # network = request.POST["network"]
  # release_date = request.POST["release_date"]
  # description = request.POST["description"]

  trip.save()

  return redirect("/trips/" + str(trip_id))
# ======================================================================================================================