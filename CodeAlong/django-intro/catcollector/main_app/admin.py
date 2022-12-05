from django.contrib import admin
from .models import Cat, Feeding

# Register your models here.

# you can use the super user by going to /admin & logingin with the super user info
admin.site.register(Cat)
admin.site.register(Feeding)