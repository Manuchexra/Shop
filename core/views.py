from django.shortcuts import render

def index(request):
    return render(request, 'Delicious/index.html')
