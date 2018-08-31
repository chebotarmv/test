from django.db import models


class Urls(models.Model):
    short_id = models.SlugField(max_length=6, primary_key=True)
    httpurl = models.URLField(max_length=200)
    date = models.DateTimeField(auto_now=True)


def __str__(self):
    return self.httpurl