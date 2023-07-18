from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
## Create your views here.

def display_form(request):
    SUFO=SignUpForm()
    d={'SUFO':SUFO}

    if request.method == 'POST':
        SUFDT=SignUpForm(request.POST)
        if SUFDT.is_valid():
            name=SUFDT.cleaned_data['age']

            # return HttpResponse(str(name))
            return HttpResponse(str(SUFDT.cleaned_data))

    return render(request,'djforms.html',d)
