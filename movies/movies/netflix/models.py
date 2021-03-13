from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200 , null=True , blank=True)

    def __str__(self):
        return f"{self.title}"


class Country(models.Model):
    name = models.CharField(max_length=200, null=True , blank=True)

    def __str__(self):
        return f"{self.name}"

        
class Rate(models.Model):
    rate = models.IntegerField(null=True, blank =True)
    def __str__(self):
        return f"{self.rate}"

class Movie(models.Model):
    title= models.CharField(max_length=200)
    desc = models.TextField()
    year = models.DateField()
    poster = models.ImageField(upload_to="movies/posters" )
    video = models.FileField(upload_to="movies/videos")
    categories = models.ManyToManyField(Category)
    country = models.ForeignKey(Country , null=True ,on_delete=models.SET_NULL)
    rate= models.OneToOneField(Rate, null=True,on_delete=models.SET_NULL)
    
