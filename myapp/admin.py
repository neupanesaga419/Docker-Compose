from django.contrib import admin
from myapp.models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id','name','description','age']
