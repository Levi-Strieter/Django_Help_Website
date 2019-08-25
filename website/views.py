from django.shortcuts import render, redirect, get_object_or_404
from django.forms import forms
from django.views.generic.edit import DeleteView
from django.utils import timezone 
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import HelpForm
from .models import HelpFormModel

# Create your views here.

def function(request,part_id =None):
    object = HelpFormModel.objects.get(id=part_id)
    object.delete()
    return render(request,'/core/asked_questions')

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

def FAQ(request):
    return render(request, 'website/FAQ.html')



# def help_form(request):
    # # if this is a POST request we need to process the form data
    # if request.method == 'POST':
    #     # create a form instance and populate it with data from the request:
    #     form = HelpForm(request.POST)
        
    #     # check whether it's valid:
    #     if form.is_valid():
    #         # process the data in form.cleaned_data as required
    #         name = form.cleaned_data['your_name']
    #         room_number = form.cleaned_data['room_number']
    #         email = form.cleaned_data['email']
    #         when = form.cleaned_data['when']
    #         subject = form.cleaned_data['subject']
    #         description = form.cleaned_data['description']

    #         context = {
    #             'name': name,
    #             'room_number': room_number,
    #             'email': email,
    #             'when': when,
    #             'subject': subject,
    #             'description': description,
    #         }

    #         # redirect to a new URL: 
    #         return render(request, 'website/asked_questions.html', context)


    # # if a GET (or any other method) we'll create a blank form
    # else:
    #     form = HelpForm()

    # return render(request, 'website/help_form.html', {'form':form})

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


def delete_model(request, id):
    obj = get_object_or_404(HelpFormModel, id=id)

    if request.method == 'POST':
        obj.delete()

    context = {
        'object': obj
    }
    return render(request, 'website/asked_questions.html', context)

def video(request):
    return render(request, 'website/videos.html')