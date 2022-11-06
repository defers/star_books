from django.shortcuts import render
from my_books.models import User

# Create your views here.


def list_users(request):
    entitys = User.objects.all()
    model = dict(entitys=entitys)
    return render(request, "books.html", context=model)
