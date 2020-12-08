from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from .models import Contact
from packages.DEM import dec,enc
from django.shortcuts import get_object_or_404

def contact(request):
    if request.method=="POST":
        name=enc(request.POST['uname'])
        email=enc(request.POST['uemail'])
        message=enc(request.POST['umessage'])
        ins = Contact(name=name,email=email,message=message)
        ins.save()
    return redirect("http://127.0.0.1:8000/")

def delete_contact(request,email):
    Contact.objects.get(email=enc(email)).delete()
    return HttpResponseRedirect("http://127.0.0.1:8000/website/inbox")


def inbox(request):
    return render(request,"templates_website/inbox.html")
    

def terms_conditions(request):
    return render(request,"templates_website/terms-conditions.html")

def privacy_policy(request):
    return render(request,"templates_website/privacy-policy.html")

def customers(request):
    return render(request,"templates_website/customers.html")

def logout(request):
    return render(request,"templates_website/logout.html")