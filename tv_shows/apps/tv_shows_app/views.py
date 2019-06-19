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
def show_info(show_id):
  # Specific show
  show = Shows.objects.get(id=show_id)

  # To pass into HTML
  return {"show": show}
# ======================================================================================================================
def new(request):
  return render(request, "tv_shows_app/new.html")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def add(request):

  if request.method != "POST":
    print("ERROR: Expecting a POST request to be made to this route")
  title = request.POST['title']
  desc = request.POST["desc"]

  # TODO: Get network, release_date, description from form
  book = Shows.objects.create(title=title)

  context = show_info(book.id) # To pass into HTML
  return render(request, "books_authors_app/show.html", context)