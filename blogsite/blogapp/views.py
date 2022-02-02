from django.shortcuts import render
from datetime import datetime
from .forms import ContactForm
from .models import Contact
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup

time = datetime.now().year
context = {
        'time': time,
        'name': 'Akshay Mohan'

    }

def Home(request):
    file = requests.get('https://www.ndtv.com/topic/top-10')
    data = file.text
    # print(data)

    soup = BeautifulSoup(data, 'html.parser')
    tit = soup.findAll(name='div', class_='src_itm-ttl')
    dis = soup.findAll(name='div', class_='src_itm-txt')
    # print(dis)

    title = [i.getText() for i in tit]
    t1=title[0]
    t2=title[1]
    t3=title[2]
    discr = [y.getText() for y in dis]
    print(discr[0])
    d1=discr[0]
    d2=discr[1]
    d3=discr[2]
    date=datetime.now().date()
    year=datetime.now().year
    context={
        'title':title ,
        't1':t1,'t2':t2,'t3':t3,
        'dis':discr,
        'd1':d1,'d2':d2,'d3':d3,
        'date':date,'name':'Akshay Mohan',
        'time':year


    }


    return render(request,'index.html',context)

def Home2(request):


    return render(request,'index.html',context)

def About(request):

    return render(request, 'about.html',context)

def contact(request):
    if request.method=='POST':

     name=request.POST.get('name')
     email = request.POST.get('email')
     phone = request.POST.get('phone')
     dis= request.POST.get('dis')
     contact=Contact(name=name,email=email,phone=phone,dis=dis)
     contact.save()

    return render(request,'contact.html',context)

def Post(request):
    return render(request,'post.html',context)




