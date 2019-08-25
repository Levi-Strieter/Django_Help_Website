from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

# # Create user and save to the database
# user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')

# # Update fields and then save again
# user.first_name = 'John'
# user.last_name = 'Citizen'
# user.save()


class HelpFormModel(models.Model):
    your_name = models.CharField(max_length=100)
    room_number = models.CharField(max_length=6)
    email = models.EmailField()
    subject = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    when = models.DateField(default=timezone.now())

    def __str__(self):
        return self.name
