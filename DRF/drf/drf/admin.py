from django.contrib import admin

from .models import MyFirstModel


@admin.register(MyFirstModel)
class MyFirstModelAdmin(admin.ModelAdmin):
    pass
