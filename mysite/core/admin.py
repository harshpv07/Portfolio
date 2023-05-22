from django.contrib import admin

# Register your models here.

from .models import ContactModel, ProjectModel, StackModel, WorkModel

admin.site.register(ContactModel) #Register the model to appear in the admin page
admin.site.register(ProjectModel)
admin.site.register(StackModel)
admin.site.register(WorkModel)