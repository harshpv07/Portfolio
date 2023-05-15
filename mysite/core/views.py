from django.shortcuts import render
from .forms import NameForm
from django.http import HttpResponseRedirect
# Create your views here.


def index(request):
    if( request.method == "POST"):
        form = NameForm(request.POST)
        if form.is_valid():
            print(request.POST.get("your_name"))
    else:
        form = NameForm()
 
    return render(request , 'core/index.html' , {"form": form})


def base(request):
    return render(request , 'core/base.html')