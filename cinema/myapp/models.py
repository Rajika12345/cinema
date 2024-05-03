from django.db import models

# Create your models here.
class Movie(models.Model):#pascalcase
    title=models.CharField(max_length=200,unique=True)
    director=models.CharField(max_length=200)
    year=models.CharField(max_length=200)
    genres=models.CharField(max_length=200)
    poster=models.ImageField(upload_to='images',default='images/default.jpg',blank=True)
    actors=models.CharField(max_length=200)
    run_time=models.PositiveIntegerField() #snakecase
    description=models.CharField(max_length=200,null=True)
    writers=models.CharField(max_length=200)
    language=models.CharField(max_length=200)

    def __str__(self):
        return self.title
    