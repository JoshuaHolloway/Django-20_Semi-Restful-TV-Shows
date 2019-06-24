from django.db import models
# ======================================================================================================================
# Create your models here.
class Trips(models.Model):

  # TODO: Change to destination
  dest = models.CharField(max_length=64)
  start_date = models.DateTimeField(auto_now=True)
  end_date   = models.DateTimeField(auto_now=True)
  plan = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __repr__(self):
    return f"Trips: ({self.dest}, {self.start_date}, {self.end_date}, {self.plan})"
# ======================================================================================================================