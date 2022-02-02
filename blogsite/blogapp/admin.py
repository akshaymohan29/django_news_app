from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
 list=['name','email','phone','dis']
admin.site.register(Contact)
