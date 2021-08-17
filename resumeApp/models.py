from django.db import models
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Resume(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    bio = RichTextField()
    


    def __str__(self):
       return '{} {}'.format(self.first_name, self.last_name)