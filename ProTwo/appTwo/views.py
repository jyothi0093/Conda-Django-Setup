from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("<em>My second project</em>")

def help(request):
    helpdict = {'help_inserts':"HELP PAGE"}
    return render(request,'appTwo/help.html',context=helpdict)

# Create your views here.
