from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(default="....", max_length=100)
    texte = models.TextField(default="...")
    author = models.CharField(max_length=100, default="Alphonse Muhindo Valivambene")
    image = models.ImageField(default="{% static 'images/logo.png' %}", null=True, blank=True)
    email = models.EmailField(default="valivambenealphonse@gmail.com")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url