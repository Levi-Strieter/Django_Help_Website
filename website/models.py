from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

# # Create user and save to the database
# user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')

# # Update fields and then save again
# user.first_name = 'John'
# user.last_name = 'Citizen'
# user.save()

FAQ_CHOICES = (
    ('ipad', 'Ipad'),
    ('mac', 'Mac'),
    ('keynote', 'Keynote'),
    ('pages', 'Pages'),
    ('imovie', 'Imovie'),
    ('schoology', 'Schoology'),
    ('other', 'Other'),
)

LIKE_DISLIKE = (
    ('like', 'Like'),
    ('dislike', "Dislike"),
)


class HelpFormModel(models.Model):
    your_name = models.CharField(max_length=100)
    room_number = models.CharField(max_length=6)
    email = models.EmailField(default="@k12.wv.us")
    subject = models.CharField(max_length=30)
    description = models.TextField()
    date_uploaded = models.DateField(default=now())

    def __unicode__(self):
        return self.Name + ": " +str(self.id)


class FaqFormModel(models.Model):
    subject = models.CharField(max_length=10, choices=FAQ_CHOICES, default="other")
    question = models.CharField(max_length=50, default="")
    answer = models.TextField()
    date_uploaded = models.DateField(default=now())

    def __unicode__(self):
        return self.Name + ": " +str(self.id)


class VideoFormModel(models.Model):
    subject = models.CharField(max_length=10, choices=FAQ_CHOICES, default="other")
    youtube_unique_code = models.CharField(max_length=11)
    vid_name = models.CharField(max_length=50, blank=False, default="Core Help-")

    def __unicode__(self):
        return self.Name + ": " +str(self.id)

# class FaqLikeModel(models.Model):
#     like = models.CharField(max_length=8,  choices=LIKE_DISLIKE, widget=forms)
#     dislike = models.CharField(max_length=8,  choices=LIKE_DISLIKE)

#     def __unicode__(self):
#         return self.Name + ": " +str(self.id)
