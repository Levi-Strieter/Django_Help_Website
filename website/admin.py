from django.contrib import admin

from .models import HelpFormModel, FaqFormModel 
# Register your models here.

admin.site.register(HelpFormModel)
admin.site.register(FaqFormModel)