from django.shortcuts import render

# Create your views here.

def usage(request):
    return render(request,'usage.html')