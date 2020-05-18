from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home2(request):
    my_dict = {'hii_Lakhan':"this is my best friend"}
    return render(request,'home2.html',context =my_dict)

def add(request):

    val1 = int(request.POST['val1'])
    val2 = int(request.POST['val2'])
    val3 = int(request.POST['val3'])
    res = val1 + val2 + val3
    return render(request,'result.html',{'result':res})