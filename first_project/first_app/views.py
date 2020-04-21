from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    #return HttpResponse("Hellow world!!")
    my_dict = {'insert_me':"Hello I am from first aopp/index.html"}
    return render(request,'first_app/index.html',context=my_dict)

# Create your views here.
