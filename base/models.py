from django.db import models

# Create your models here.


    
class Movie(models.Model):
    POOR = 'Poor'
    MEH = 'Meh'
    MID = 'Mid'
    DECENT = 'Decent'
    RAD = 'Rad'
    Rating = [
       (POOR, ('Poor')),
       (MEH, ('Meh')),
       (MID, ('Mid')),
       (DECENT, ('Decent')),
       (RAD, ('Rad')),
    ]
    RELEASED = 'Released'
    EXPECTED = 'Expected'
    Status = [
       (RELEASED, ('Released')),
       (EXPECTED, ('Expected')),
    ]
    Hollywood = 'Hollywood'
    Bollywood = 'Bollywood'
    Korean = 'Korean'
    African = 'African'
    European = 'European'
    Country = [
       (Hollywood, ('Hollywood')),
       (Bollywood, ('Bollywood')),
       (Korean, ('Korean')),
       (African, ('African')),
       (European, ('European')),
    ]
    Thriller = 'Thriller'
    Action = 'Action'
    Comedy = 'Comedy'
    Drama = 'Drama'
    Genre = [
       (Thriller, ('Thriller')),
       (Action   , ('Action')),
       (Drama, ('Drama')),
       (Drama   , ('Drama')),
    ]
    title = models.CharField(max_length=50)
    synopsis = models.TextField()
    genre = models.CharField(max_length=10, choices=Genre, null=True)
    industry = models.CharField(max_length=10, choices=Country, null=True)
    rating = models.CharField(max_length=10, choices=Rating, null=True)
    poster = models.ImageField(upload_to='media')
    release_year = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    trailer = models.FileField(upload_to='media',  null=True)
    status = models.CharField(max_length=10, choices=Status, null=True)
    price = models.FloatField(null=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

class Comment(models.Model):
    POOR = 'poor'
    MEH = 'meh'
    MID = 'mid'
    DECENT = 'decent'
    RAD = 'rad'
    Rating = [
       (POOR, ('Poor')),
       (MEH, ('Meh')),
       (MID, ('Mid')),
       (DECENT, ('Decent')),
       (RAD, ('Rad')),
    ]
    author = models.CharField(max_length=25)
    rating = models.CharField(max_length=50, choices=Rating, null=True)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.author
