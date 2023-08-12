
import json
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
from django.shortcuts import redirect, render,HttpResponse,HttpResponseRedirect
from my_app.models import Contact,myUser,Post,multipleImage
from my_app.forms import uploadPostForm,multipleImageForm
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
def signUp(request):
    name = None
    
    if 'name' in request.COOKIES:
        name = request.COOKIES['name']
        return render(request, 'home.html', {'name': name})

    if request.method == 'POST':
        form = uploadPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Post uploaded successfully")

            name = request.POST.get('name')
            response = redirect('home')
            response.set_cookie('name', name)  # Set the 'name' cookie
            return response
    else:
        form = uploadPostForm()

    return render(request, 'signup.html', {'form': form, 'name': "Welcome"})


def logout(request):
        response = HttpResponseRedirect('/signup')
        response.delete_cookie('name')
        return response
def multipleImageUpload(request):
    images=multipleImage.objects.all()
    print(serializers.serialize('json',images))
    if request.method == 'POST':
        form = multipleImageForm(request.POST, request.FILES)
        if form.is_valid():
            for image in request.FILES.getlist('images'):
                    multipleImage.objects.create(images=image)
            
            form.save()     
            messages.success(request, "Images uploaded successfully")
            return redirect('multipleImageUpload')
        else:
            print("invalid")
            print(form.errors)
       
    else:
        form = multipleImageForm()

    return render(request, 'multipleImageUpload.html', {'form': form,'images':images})

