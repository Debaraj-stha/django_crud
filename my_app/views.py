
import json
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
from django.shortcuts import redirect, render,HttpResponse
from my_app.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.http import require_POST
# Create your views here.
def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request,'services.html')
def home(request,):
    context={
       "name":"Jeevan"
    }
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'index.html',context)

def getAllContact(request):
# Retrieve all Contact objects
    contacts = Contact.objects.all()
    contacts_json = serializers.serialize('json', contacts)
    if request.method == 'POST':
            name=request.POST.get("name")
            email=request.POST.get("email")
            pk=request.POST.get("pk")
            print("name",name)
            contact=Contact.objects.get(pk=pk)
            contact.name=name
            contact.email=email
            contact.password="devar"
            contact.save()
            messages.success(request,"fcontact updated successfully")
            return render(request, 'myContacts.html',{'contacts':contacts_json})
   
    return render(request, 'myContacts.html',{'contacts':contacts_json})

def contact(request):
   if request.method=="POST":
       name=request.POST.get("name")
       email=request.POST.get("email")
       password=request.POST.get("password")
       contact=Contact(name=name,email=email,password=password)
       contact.save()
       messages.success(request,"form submitted successfully")

   return render(request,'contact.html')
def updateContact(request):
    print(request.method)
    if request.method == 'POST':
        
            data=json.loads(request.body)
          
            contact=Contact.objects.get(pk=data['pk'])
            contact.name=data['name']
            contact.email=data['email']
            contact.save()
        
            return JsonResponse({"message":"contact updated successfully"})
       
    return HttpResponse("Contact updated successfully")
def deleteContact(request,id):
      print("id",id)
      contact = Contact.objects.get(pk=id)
      contact.delete()
      contacts = Contact.objects.all()
      contacts_json = serializers.serialize('json', contacts)
      messages.success(request,"Contact deleted successfully")
      return JsonResponse({messages: "success"})
     
def logoutUser(request):
    logout(request)
    return redirect('/login')
