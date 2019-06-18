from django.shortcuts import render, HttpResponse
from .models import Shows

def index(request):

  context = {"shows": Shows.objects.all()}
  return render(request, "tv_shows_app/index.html", context)