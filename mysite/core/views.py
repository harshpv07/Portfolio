from django.shortcuts import render
from .forms import NameForm
from django.http import HttpResponseRedirect
from django.conf import settings
from .models import ContactModel, StackModel, ProjectModel
import os



def index(request):
    if( request.method == "POST"): #Check if it is a post request
        name = request.POST.get("your_name") #Get the value of the field "your_name" from the request
        email = request.POST["your_email"]
        phone = request.POST["your_phone"]
        query = request.POST["your_query"]
        insertclass = ContactModel(name = name , email = email , query = query , contact = phone) #pass it as parameters to the Model class to store it in the internal DB
        insertclass.save() #Save the entry into the DB
        context = {}

        # Join images directory to index.html view
        flags = (os.listdir(os.curdir + "/core/static/stack_images"))

        # This adds the images to the output dict
        flags = ['stack_images/'+fl for fl in flags]
        b = ProjectModel.objects.all().filter()
        for k in b: 
            print(k.project_date , k.project_descrip, k.proj_image)

        context['flags'] = flags
        print(context)

    return render(request , 'core/index.html' , context)

def base(request):
    return render(request , 'core/base.html')