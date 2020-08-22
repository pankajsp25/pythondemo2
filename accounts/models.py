from django.contrib.auth.models import User

# Create your models here.
from django.db import models

from master.models import CannabisSmoke, Education, Hobbies, Religion


class Profile(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    R_STATUS = (
        ('Single', 'Single'),
        ('In a relationship', 'In a relationship'),
        ('Married', 'Married'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='profile_pic')
    gender = models.CharField(choices=GENDER, null=True, blank=True, max_length=20)
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    zip = models.CharField(max_length=10, null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    education = models.ForeignKey(Education, on_delete=models.SET_NULL, blank=True, null=True)
    religion = models.ForeignKey(Religion, on_delete=models.SET_NULL, blank=True, null=True)
    relationship_status = models.CharField(choices=R_STATUS, max_length=100, blank=True, null=True)
    smoke_ciggarettes = models.BooleanField(blank=True, null=True)
    drink = models.BooleanField(blank=True, null=True)
    smoke_marijuana = models.BooleanField(blank=True, null=True)
    hobbies = models.ManyToManyField(Hobbies, blank=True, null=True)
    favourite_cannabis_smoke = models.ManyToManyField(CannabisSmoke, null=True, blank=True, related_name='profiles')

    def __str__(self):
        return self.user.get_full_name()
