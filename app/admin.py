from django.contrib import admin
from .models import Person, Duty

# Register your models here.
admin.site.register(Duty)
admin.site.register(Person)