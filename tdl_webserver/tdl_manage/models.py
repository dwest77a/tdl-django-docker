from django.db import models

# Create your models here.
class Item(models.Model):
    order_ID = models.CharField(max_length=3)
    project  = models.CharField(max_length=30)
    # format, current, stage, dependencies
    iformat  = models.CharField(max_length=20)
    current  = models.CharField(max_length=300)
    stage    = models.CharField(max_length=5)
    dependencies = models.CharField(max_length=30)
    status   = 