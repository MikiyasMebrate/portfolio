from django.shortcuts import render
from django.contrib import messages
from .models import (
    Education,
    Project,
    History,
    Portfolio
    )
from .forms import (
    ContactUsForm
)
# Create your views here.
def index(request):
    education = Education.objects.all()
    project = Project.objects.all()
    history = History.objects.all()
    cv = Portfolio.objects.all().first()

    form = ContactUsForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            form =  ContactUsForm()
            messages.success(request, 'Successfully sent')
        else:
            messages.error(request, 'your request has not been successfully, please try again.')


    
    context = {
        'educations' : education,
        'projects' : project,
        'history' : history,
        'form' : form,
        'cv' : cv,
    }
    return render(request, 'index.html', context=context)