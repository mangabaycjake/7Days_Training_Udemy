from django.shortcuts import render

# Create your views here.
##  Adress the location of the html file, assign function
def index(request):
    return render(request, 'myapp/index.html')

def aboutus(request):
    return render(request, 'myapp/aboutus.html')

def contactus(request):
    return render(request, 'myapp/contactus.html')
