#   Django
from django.contrib import admin

#    Models 
from .models import Todo

# Register your models here.
admin.site.register(Todo)