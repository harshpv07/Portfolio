from django.shortcuts import render
from .forms import NameForm
from django.http import HttpResponseRedirect
from django.conf import settings
from .models import ContactModel, StackModel, ProjectModel
import os



def index(request):
    context = {}

    # Join images directory to index.html view
    flags = (os.listdir(os.curdir + "/core/static/stack_images"))

    # This adds the images to the output dict
    flags = ['stack_images/'+fl for fl in flags]
    b = ProjectModel.objects.all().filter()
    projects = []
    for k in b: 
        projects.append({"proj_name" : k.proj_name , "project_descrip" : k.project_descrip, "proj_image" : k.proj_image , "proj_related" : k.proj_related})
        
    context["project"] = projects
    context['flags'] = flags
    
    if( request.method == "POST"): #Check if it is a post request
        name = request.POST.get("your_name") #Get the value of the field "your_name" from the request
        email = request.POST["your_email"]
        phone = request.POST["your_phone"]
        query = request.POST["your_query"]
        insertclass = ContactModel(name = name , email = email , query = query , contact = phone) #pass it as parameters to the Model class to store it in the internal DB
        insertclass.save() #Save the entry into the DB
        
        return render(request , 'core/index.html')
    
    return render(request , 'core/index.html' , context)

def base(request):
    return render(request , 'core/base.html')