from django.contrib import admin
from burgers.models import Burger

@admin.register(Burger)
class BurgerAmdin(admin.ModelAdmin):
    pass

# Register your models here.
