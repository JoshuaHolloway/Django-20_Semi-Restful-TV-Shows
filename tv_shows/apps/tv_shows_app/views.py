from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Trips, Users
# ======================================================================================================================
def root(request):

  # Initialize session
  if 'user_logged_in' not in request.session:
    request.session['user_logged_in'] = {}
  return redirect("/users/reg_login")


  # TODO: Change this to Login Screen
  #  -After login, then redirect to /trips
  #return redirect("/trips")
# ======================================================================================================================
def trips(request):
  # All Trips
  trips = Trips.objects.all()

  # Current User
  user = Users.objects.get(id = request.session['user_logged_in']['id'])
  context = {'trips': trips, 'user': user}
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

  # Step 0: Grab info from form
  dest = request.POST['dest']

  # TODO: Grab other fields
  # start_date = request.POST["start_date"]
  # end_date = request.POST["end_date"]
  # plan = request.POST["plan"]
  plan = "temp plan"

  # TODO: Apply the one-to-many relationship
  # Step 1: Grab user row from Users table
  user_id = request.session['user_logged_in']['id'] # Grab user-id
  user = Users.objects.get(id=user_id)

  # Step 2: Create row in Trips table
  #trip = Trips.objects.create(dest=dest, start_date='2019-06-06', plan="temp")
  trip = Trips.objects.create(dest=dest, plan=plan, user=user)

  # Step 3: Pass data into HTML
  trips = Trips.objects.all()
  users = Users.objects.all()
  context = {'trips': trips, 'users': users}

  return render(request, "tv_shows_app/index.html", context)
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
  dest = request.POST['dest']
  trip.dest = dest # TODO

  # TODO
  # network = request.POST["network"]
  # release_date = request.POST["release_date"]
  # description = request.POST["description"]

  trip.save()

  return redirect("/trips/" + str(trip_id))
# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================
# =LOGIN and REGISTRATION below=========================================================================================
# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================
def reg_login(request):
  return render(request, "tv_shows_app/reg_login.html")
# ======================================================================================================================
def validate(request):

  # Return true if no errors
  valid = False

  # pass the post data to the method we wrote and save the response in a variable called errors
  errors = Users.objects.basic_validator(request.POST, Users.objects.all())

  # check if the errors dictionary has anything in it
  if len(errors) > 0:

    # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
    for key, value in errors.items():
      messages.error(request, value)

    # Errors found
    return valid

  else:
    # No erros => Valid
    valid = True
    return valid
# ======================================================================================================================
def register(request):

  valid = validate(request)
  if valid:

    # Grab values from form
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password_orig = request.POST['password']

    # Hash Password
    password_hash = bcrypt.hashpw(password_orig.encode(), bcrypt.gensalt())

    # Create row in database
    user = Users.objects.create(
      first_name=first_name,
      last_name=last_name,
      email=email,
      password_hash=password_hash)

    messages.success(request, "Successfully registered")
    return redirect("/users/reg_login")
  else: # not-valid
    # redirect the user back to the form to fix the errors
    return redirect("/users/reg_login")
# ======================================================================================================================
import bcrypt
def login(request):

  # Grab email from form
  email = request.POST['email-login']

  # Grab row from database
  user = Users.objects.get(email=email)

  # Grab entered password and test against stored hash
  password_login = request.POST['password-login']
  if bcrypt.checkpw(password_login.encode(), user.password_hash.encode()):
    print("password match")

    # Set Session with logged-in users info
    request.session['user_logged_in'] = {
      'id': user.id,
      'first_name': user.first_name,
      'logged_in': True
    }

    # return render(request, "login_reg_app/logged_in.html", {'user': user})
    return redirect("/trips")
  else:
    print("failed password")
    return HttpResponse("You Loose!")
# ======================================================================================================================
def logout(request):
  request.session.pop('user_logged_in')
  return redirect("/")
# ======================================================================================================================