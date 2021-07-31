from django.db import models

# Create your models here.
class Crud(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    created = models.DateField(auto_created=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
