from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Trips, Users

# ======================================================================================================================
def root(request):
  if 'user_logged_in' not in request.session:
    request.session['user_logged_in'] = {} # Initialize session
  return redirect("/users/reg_login")
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
# ======================================================================================================================
def validate(request, Model):

  # Return true if no errors
  valid = False

  # pass the post data to the method we wrote and save the response in a variable called errors
  errors = Model.objects.basic_validator(request.POST, Model.objects.all())

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
def new(request):
  return render(request, "tv_shows_app/new.html")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def add(request):

  valid = validate(request, Trips)
  if valid:
    # Step 0: Grab info from form
    dest = request.POST['dest']
    start_date = request.POST["start_date"]
    end_date = request.POST["end_date"]
    plan = request.POST["plan"]

    # Step 1: Grab user row from Users table
    user_id = request.session['user_logged_in']['id'] # Grab user-id
    user = Users.objects.get(id=user_id)

    # Step 2: Create row in Trips table
    trip = Trips.objects.create(dest=dest, plan=plan, start_date=start_date, end_date=end_date, user=user)

    # Step 3: Pass data into HTML
    trips = Trips.objects.all()
    user = Users.objects.get(id=request.session['user_logged_in']['id'])
    context = {'trips': trips, 'user': user}
    return render(request, "tv_shows_app/index.html", context)

  else: # not-valid
    # redirect the user back to the form to fix the errors
    return redirect("trips/new")
# ======================================================================================================================
def delete(request, trip_id):
  Trips.objects.get(id=trip_id).delete()
  return redirect("/trips")
# ======================================================================================================================
def edit(request, trip_id):
  return render(request, "tv_shows_app/edit.html", get_trip_info(trip_id))
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def apply_edit(request, trip_id):

  valid = validate(request, Trips)
  if valid:
    trip = Trips.objects.get(id=trip_id)
    trip.dest = request.POST['dest']
    trip.start_date = request.POST["start_date"]
    trip.end_date = request.POST["end_date"]
    trip.plan = request.POST["plan"]
    trip.save()
    return redirect("/trips") # redirect to dashboard

  else: # not-valid
    ## redirect the user back to the form to fix the errors
    #redirect_path = "trips/edit/" + str(trip_id)
    #print(redirect_path)
    #return redirect(redirect_path) # TODO: Why does this route to trips/5/edit/trips/edit/5 ????
    return render(request, "tv_shows_app/edit.html", get_trip_info(trip_id)) # HACK TODO: Replace with actual redirect
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
def register(request):

  #valid = validate_user(request)
  valid = validate(request, Users)
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