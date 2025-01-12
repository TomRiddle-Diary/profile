from django.shortcuts import render

def home(request):
    return render(request, 'myprofile/home.html')

def activity(request):
    return render(request, 'myprofile/activity.html')
