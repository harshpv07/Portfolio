from django.contrib import admin

# Register your models here.

from .models import ContactModel

admin.site.register(ContactModel) #Register the model to appear in the admin page