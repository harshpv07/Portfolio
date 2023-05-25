from django.db import models

# Create your models here.

class ContactModel(models.Model): #DB model for the customer queries
    name = models.CharField(max_length= 100)
    email = models.CharField(max_length=100)
    query = models.CharField(max_length=500)
    contact = models.CharField(max_length=20)
    
    class Meta:
        verbose_name_plural = "ContactModel" #Django tends to add an 's' in the models page. We are trying to maintain it. 
    
    def __str__(self):
        return self.name
    


class ProjectModel(models.Model): #DB model for my project details
    proj_name = models.CharField(max_length = 100)
    project_date = models.CharField(max_length = 100)
    project_descrip = models.CharField(max_length = 100)
    proj_related = models.CharField(max_length = 100)
    proj_image = models.ImageField()
    class Meta:
        verbose_name_plural = "ProjectModel" #Django tends to add an 's' in the models page. We are trying to maintain it. 
    
    def __str__(self):
        return self.proj_name


class StackModel(models.Model): #DB model for my tech stack details
    stack_name = models.CharField(max_length= 100)
    stack_image = models.ImageField()
    class Meta:
        verbose_name_plural = "Stack_Name" #Django tends to add an 's' in the models page. We are trying to maintain it. 
    
    def __str__(self):
        return self.stack_name
    

class WorkModel(models.Model): #DB model for my work ex details
    work_name = models.CharField(max_length=100)
    work_image = models.ImageField()
    work_role = models.CharField(max_length = 100)
    class Meta:
        verbose_name_plural = "Work Name" #Django tends to add an 's' in the models page. We are trying to maintain it. 
    
    def __str__(self):
        return self.work_name



    

    