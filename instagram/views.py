from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Image,Profile

# Create your views here.

def Post(request):
    images=Image.objects.all()
    return render(request,'all-photos/images.html',{"images":images})