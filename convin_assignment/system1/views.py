from django.shortcuts import render
from .signals import save_file
from django.http import HttpResponse
from .models import File

# Create your views here.


def home(request):
    files = File.objects.all()
    context = {'files': files}
    return render(request, 'home.html', context)