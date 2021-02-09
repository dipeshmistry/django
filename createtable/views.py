from django.shortcuts import render
from .models import Contactus
#from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def home(request):
    return render(request, "contact.html")

def contact(request):
    if request.method == "POST":
        print("this is contact post")
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        print(name,email,phone,desc)
        ins = Contactus( name=name, email=email, phone=phone, desc=desc)
        ins.save()
        print("the data has been written to the db")

    return render(request, "table.html",{'name':name,'email':email,'phone':phone,'desc':desc})

def table(request):
    if request.method == "POST":
        print("this is table post")
        schemaname = request.POST['schemaname']
        tabname = request.POST['tabname']
        numofcol = request.POST['numofcol']
        print(schemaname,tabname,numofcol)
        

    return render(request, "result.html",{'schema':schemaname, 'tab':tabname, 'num':numofcol })
