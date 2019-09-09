import datetime

# class HelpForm(forms.Form):
#     your_name = forms.CharField(label='Your Name', max_length=100)
#     room_number = forms.CharField(label='Room Number', max_length=6)
#     email = forms.EmailField()
#     subject = forms.CharField(label='subject', max_length=30)
#     description = forms.CharField(label='Description', max_length=50)
#     when = forms.DateField(initial=datetime.date.today)
    
from django.forms import ModelForm
from .models import HelpFormModel, FaqFormModel, VideoFormModel
 
class HelpForm(ModelForm):
    class Meta:
        model = HelpFormModel
        fields = ['your_name', 'room_number', 'email', 'subject', 'description', 'date_uploaded']

class FaqForm(ModelForm):
    class Meta:
        model = FaqFormModel
        fields = ['subject', 'question', 'answer', 'date_uploaded']

class VideoForm(ModelForm):
    class Meta:
        model = VideoFormModel
        fields = ['subject', 'youtube_unique_code', 'vid_name']

# class FaqLikeForm(ModelForm):
#     class Meta:
#         model = FaqLikeModel
#         fields = ['like', 'dislike']
