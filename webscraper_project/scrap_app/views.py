from django.shortcuts import render,HttpResponseRedirect
from .models import Links
# Create your views here.
import requests
from bs4 import BeautifulSoup

def home(request):
    if request.method=='POST':
        new_link=request.POST.get('page','')
        urls=requests.get(new_link)
        beautysoup=BeautifulSoup(urls.text,'html.parser')
        for link in beautysoup.find_all('a'):
            li_address=link.get('href')
            li_name=link.string
            Links.objects.create(address=li_address,stringname=li_name)
            return HttpResponseRedirect('/')
    else:
     data_values=Links.objects.all()
    return render(request,'home.html',{'data_values':data_values})