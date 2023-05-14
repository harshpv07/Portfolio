from django.shortcuts import render
 
# Create your views here.


def index(request):
    project_names = {"project_names" : ["PAB" , "Assitant for the blind" , "http://temp.com"]}
    project_course_revalance = ["VIT" , "Siam internshp" , "Cisco" , "Novartis"]
    return render(request , 'core/index.html' , project_names)


def base(request):
    return render(request , 'core/base.html')