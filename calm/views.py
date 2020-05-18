from django.shortcuts import render
from django.http import HttpResponse

 Create your views here.

 def home(request):
     return render(request,'home.html',{'link':'http://127.0.0.1:8000/'})
