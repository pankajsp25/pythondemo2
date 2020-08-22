from django.db import models

# Create your models here.


class Education(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Religion(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Hobbies(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class CannabisSmoke(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


