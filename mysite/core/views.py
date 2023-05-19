from django.shortcuts import render
from .forms import NameForm
from django.http import HttpResponseRedirect
# Create your views here.

from .models import ContactModel


# def pushdata(request):   #Some issues with this. Please check this once again
#     if(request.method == "POST"):
#         name = NameForm(request.POST["your_name"])
#         email = NameForm(request.POST["your_email"])
#         phone = NameForm(request.POST["your_phone"])
#         query = NameForm(request.POST["your_query"])
#         insertclass = ContactModel(name = name , email = email , query = query , contact = phone)
#         insertclass.save()
#     return render(request , "core/pushdata.html")



def index(request):
    if( request.method == "POST"): #Check if it is a post request
        name = request.POST.get("your_name") #Get the value of the field "your_name" from the request
        email = request.POST["your_email"]
        phone = request.POST["your_phone"]
        query = request.POST["your_query"]
        insertclass = ContactModel(name = name , email = email , query = query , contact = phone) #pass it as parameters to the Model class to store it in the internal DB
        insertclass.save() #Save the entry into the DB
 
    return render(request , 'core/index.html')

def base(request):
    return render(request , 'core/base.html')