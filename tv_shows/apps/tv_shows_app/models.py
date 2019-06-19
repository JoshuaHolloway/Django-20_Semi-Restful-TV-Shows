from django.db import models
# ======================================================================================================================
# Create your models here.
class Shows(models.Model):
  title = models.CharField(max_length=64)
  # network = models.CharField(max_length=32)
  # release_date = models.DateTimeField()
  # description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __repr__(self):
    return f"Book: ({self.title})"
    #return f"Book: ({self.title}, {self.network}, {self.release_date}, {self.description})"
# ======================================================================================================================