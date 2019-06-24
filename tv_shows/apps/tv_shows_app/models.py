from django.db import models
# ======================================================================================================================
# Create your models here.
class Trips(models.Model):

  # TODO: Change to destination
  title = models.CharField(max_length=64)

  #TODO: Add in Trips attributes
  # release_date = models.DateTimeField()
  # description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __repr__(self):
    return f"Trips: ({self.title})" # TODO: Change printout
    #return f"Book: ({self.title}, {self.network}, {self.release_date}, {self.description})"
# ======================================================================================================================