from django.contrib import admin
from .models import Sauce
from .models import Food

# Register your models here.
admin.site.register(Sauce)
admin.site.register(Food)
