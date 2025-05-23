from django.db import models
from cloudinary.models import CloudinaryField

class Author(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField("image", null=True)

    def __str__(self):
        return self.title

class Subscriber(models.Model):
    email = models.EmailField()
    ceated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email