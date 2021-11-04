from django.contrib import admin
# import your models here
from .models import Pokemon, Training

# Register your models here
admin.site.register(Pokemon)
admin.site.register(Training)