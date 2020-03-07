from django.shortcuts import render

# Create your views here.
def index(request):
    mydic = {'insert_me': "Hello I'm coming from templates/help.py"}
    return render(request, 'help.html', context = mydic)