from django.shortcuts import render
from myapp.models import Person


def index(request):
    query_person = Person.objects.all()

    return render(request, 'index.html',{"persons":query_person})
