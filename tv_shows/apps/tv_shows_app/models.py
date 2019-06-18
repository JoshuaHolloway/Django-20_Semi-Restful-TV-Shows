from django.db import models
# ======================================================================================================================
# Create your models here.
class TV_show(models.Model):
  title = models.CharField(max_length=50)
  # newtork = models.CharField(max_length=255)
  # release_date = models.DateTimeField()
  # desc = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __repr__(self):
    return f"Book: ({self.title})"
# ======================================================================================================================