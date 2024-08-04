from django.db import models

# Create your models here.
# the blogpost model
class BlogPost(models.Model):
    title=models.CharField(max_length=200)
    content=models.CharField(max_length=500)
    date_added=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.content