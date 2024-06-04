from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request,"index.html")
def non (request):
    return render(request,"ben.html")
