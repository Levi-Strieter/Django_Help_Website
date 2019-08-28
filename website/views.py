from django.shortcuts import render, redirect, get_object_or_404
from django.forms import forms
from django.views.generic.edit import DeleteView
from django.utils import timezone 
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import HelpForm, FaqForm, VideoForm
from .models import HelpFormModel, FaqFormModel, VideoFormModel

# Create your views here.

def thanks(request):
    return render(request, 'website/thanks.html')

def index(request):
    return render(request, 'website/index.html')


@login_required
def asked_questions(request):

    data = HelpFormModel.objects.all()

    context = {
        'data': data,
    }

    return render(request, 'website/asked_questions.html', context)

def about_us(request):
    return render(request, 'website/about_us.html')

def FAQ(request):

    data = FaqFormModel.objects.all()

    context = {
        'data': data,
    }

    return render(request, 'website/FAQ.html', context)


def help_form(request):
    if request.method == "POST":
        form = HelpForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/core/thanks/')
 
    else:
 
        form = HelpForm()
 
        return render(request, "website/help_form.html", {'form': form})

@login_required
def FAQ_upload(request):
    if request.method == "POST":
        form = FaqForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/core/thanks/')
 
    else:
 
        form = FaqForm()
 
        return render(request, "website/FAQ_upload.html", {'form': form})

def video(request):

    data = VideoFormModel.objects.all()

    context = {
        'data': data,
    }

    return render(request, 'website/videos.html', context)

@login_required
def team_homepage(request):
    return render(request, 'website/team_page.html')

@login_required
def video_upload(request):
    if request.method == "POST":
        form = VideoForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/core/thanks/')
 
    else:
 
        form = VideoForm()
 
        return render(request, "website/video_upload.html", {'form': form})
