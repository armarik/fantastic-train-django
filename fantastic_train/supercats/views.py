from django.shortcuts import render

# Create your views here.

def hello_cat(request):
    return render(request, 'hello_cat.html', {})