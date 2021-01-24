import datetime

from django.db import models
from django.utils import timezone
from django import forms

CATEGORIES = [
    ('convenience', 'Convenience'),
    ('fast food', 'Fast Food'),
    ('thai', 'Thai'),
    ('asian', 'Asian'),
    ('desert', 'Desert'),
    ('bubble tea', 'Bubble Tea'),
    ('bakery', 'Bakery'),
    ('healthy', 'Healthy'),
    ('indian', 'Indian'),
    ('korean', 'Korean'),
    ('japanese', 'Japanese'),
    ('chinese', 'Chinese'),
]

# Create your models here.
class VendorPost(models.Model):
    business_name = models.CharField(max_length= 100, default = ' ')
    owner_name = models.CharField(max_length = 100, default = ' ')
    business_address = models.CharField(max_length = 100, default = 'PLEASE CONTACT')
    phone_number = models.CharField(max_length = 100, default = ' ')
    email = models.CharField(max_length = 100, default = ' ')
    description = models.CharField(max_length = 350, default = ' ')
    pub_date = models.DateTimeField('date published')
    business_category1 = forms.CharField(label='business category', widget=forms.Select(choices=CATEGORIES))
    #business_category2 = forms.CharField(label='business category', widget=forms.Select(choices=CATEGORIES))
    photo = models.ImageField(null = True, blank = True)


    def __str__(self):
        return self.business_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



# this is just a placeholder to not mess things up 
class Choice(models.Model):
    vendorPost = models.ForeignKey(VendorPost, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text