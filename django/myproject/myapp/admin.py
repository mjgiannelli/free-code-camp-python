from django.contrib import admin
# in order to get your models to show up in the django admin dash
# you need to import them here
from .models import Feature

# Register your models here.
admin.site.register(Feature)
