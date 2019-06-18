from django.shortcuts import render, HttpResponse
from .models import TV_show

def index(request):

  context = {"shows": TV_show.objects.all()}
  return render(request, "tv_shows_app/index.html", context)