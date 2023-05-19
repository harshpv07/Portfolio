from django.db import models

# Create your models here.

class ContactModel(models.Model):
    name = models.CharField(max_length= 100)
    email = models.CharField(max_length=100)
    query = models.CharField(max_length=500)
    contact = models.CharField(max_length=20)
    
    class Meta:
        verbose_name_plural = "ContactModel" #Django tends to add an 's' in the models page. We are trying to maintain it. 
    
    def __str__(self):
        return self.name
    

    

    