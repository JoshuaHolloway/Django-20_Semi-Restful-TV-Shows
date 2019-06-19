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
def get_show_info(show_id):
  # Specific show
  show = Shows.objects.get(id=show_id)

  # To pass into HTML
  return {"show": show}
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
  show = Shows.objects.create(title=title)
  return render(request, "tv_shows_app/show.html", get_show_info(show.id))
# ======================================================================================================================
def delete(request, show_id):
  Shows.objects.get(id=show_id).delete()
  return redirect("/shows")
# ======================================================================================================================
def edit(request, show_id):
  return render(request, "tv_shows_app/edit.html", get_show_info(show_id))
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def apply_edit(request, show_id):

  # TODO: Change from creation to edit query
  show = Shows.objects.get(id=show_id)
  title = request.POST['title']
  show.title = title

  # TODO
  # network = request.POST["network"]
  # release_date = request.POST["release_date"]
  # description = request.POST["description"]

  show.save()

  return redirect("/shows/" + str(show_id))
# ======================================================================================================================