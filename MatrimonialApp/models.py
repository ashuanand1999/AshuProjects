from django.db import models
from multiselectfield import MultiSelectField

class RegistrationData(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    username = models.CharField(max_length=100)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=100)
    age = models.IntegerField()

    GENDER_CHOICES = (('M', 'Male'),('F', 'Female'))

    gender = MultiSelectField(max_length=30,choices=GENDER_CHOICES)

    No_of_marriage = (('1','one'),('2','two'),('3','three'))

    No_of_marriages = MultiSelectField(max_length=20,choices=No_of_marriage)

    expectation1 = (('kat','Katrina Kaif'),('deepu','Deepika Padukone'),('sunney','Sunney Leoni'))

    Expectation1 = MultiSelectField(max_length=50,choices=expectation1, null=True,blank=True)

    expectation2 = (('sallu','Salman Khan'),('sahid','Shahid Kapoor'),('ranveer','Ranveer Singh'))

    Expectation2 = MultiSelectField(max_length=50, choices=expectation2, null=True,blank=True)

    alcohol = (('no','No alcoholic'),('yes','Only on weekends'),('yes','Occasionally'))

    alcoholic_status = MultiSelectField(max_length=50,choices=alcohol)
    more_info = models.TextField(max_length=1000, null=True,blank=True)


class FeedbackData(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=50)
    rating = models.IntegerField()
    date = models.DateTimeField(max_length=100)
    feedback = models.TextField(null=True,blank=True)





