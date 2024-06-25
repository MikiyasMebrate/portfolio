from django.shortcuts import render
from .models import (
    Education,
    Project,
    History
    )

# Create your views here.
def index(request):
    education = Education.objects.all()
    project = Project.objects.all()
    history = History.objects.all()
    
    context = {
        'educations' : education,
        'projects' : project,
        'history' : history,
    }
    return render(request, 'index.html', context=context)