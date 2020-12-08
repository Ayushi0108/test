from django.http import HttpResponse
from authentication.models import Register,Payment
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from packages.DEM import dec,enc
import random
import datetime

# Create your views here.

otp_global = 0
register = None
email = ''
prize = 0
def login(request,prize):
    globals()['prize'] = prize
    if request.method == 'POST':
        globals()['email'] = enc(request.POST['email'])
        password = enc(request.POST['password'])
        try:
            globals()['register'] = Register.objects.get(email = globals()['email'])        
            if globals()['register'].password != password:
                err_msg = "Incorrect Password"
                return render(request,'templates_authentication/index.html',{'err_msg':err_msg,'prize':globals()['prize']})
            else:
                if prize!=0:
                    return render(request,'templates_authentication/payment.html',{'prize': globals()['prize']})
                else:
                    return render(request,'templates_authentication/show.html')
        except ObjectDoesNotExist:
            err_msg = "Account doesn't exist"
            return render(request,'templates_authentication/index.html',{'err_msg': err_msg,'prize':globals()['prize']})
    else:
        return render(request,'templates_authentication/index.html',{'prize':globals()['prize']})      
            

def signup(request):
    if request.method == 'POST':   
        name = enc(request.POST['username'])
        globals()['email'] = enc(request.POST['email'])
        password = enc(request.POST['password'])
        #password = password.strip()
        conf = enc(request.POST['conf_pass'])
        
        try:
            globals()['register'] = Register.objects.get(email = globals()['email'])
            err_message = "Account already exists"
            return render(request,'templates_authentication/signup.html',{'err_message':err_message,'prize':globals()['prize']})
        except ObjectDoesNotExist:
            if len(password) <=4 or len(password)>16:
                    err_pass = "Password must be more than 4 and less than 16 characters"
                    return render(request,'templates_authentication/signup.html',{'err_pass':err_pass,'prize':globals()['prize']})
            else:
                if password == conf:
                    
                    globals()['register'] = Register(name=name,email=globals()['email'],password=password)
                    comm_otp_generation()
                    return render(request,'templates_authentication/otp.html')
                else:
                    err_pass = "Passwords doesn't match"
                    return render(request,'templates_authentication/signup.html',{'err_pass':err_pass,'prize':globals()['prize']})
    else:
        return render(request,'templates_authentication/signup.html',{'prize':globals()['prize']})      
            
        
         
def verify(request):
    err_msg = ""
    try:
        if request.method == 'POST':
            try:
                otp = int(request.POST.get('otp',0))
                if globals()['otp_global'] == otp:
                    globals()['register'].save()
                    return render(request,'templates_authentication/index.html',{'prize':globals()['prize']})             
                else:
                    err_msg = "Incorrect OTP"
                    return render(request,'templates_authentication/otp.html',{'err_msg':err_msg})
            except ValueError:
                err_msg = "Only characters allowed"
                return render(request,'templates_authentication/otp.html',{'err_msg':err_msg})

    except IntegrityError as e:
        err_msg = "Account already exists"
        return render(request,'templates_authentication/otp.html',{'err_msg':err_msg})


def generate(request):        
    comm_otp_generation()
    return render(request,'templates_authentication/otp.html')

def change_pass(request):
    if request.method == 'POST':
        globals()['email'] = enc(request.POST['email'])
        password = enc(request.POST['pass'])
        conf_pass = enc(request.POST['conf_pass'])

        try:
            globals()['register'] = Register.objects.get(email = globals()['email'])
            if password == conf_pass:
                if len(password) <=4 or len(password)>16:
                    err_msg = "Password must be more than 4 and less than 16 characters"
                    return render(request,'templates_authentication/changepass.html',{'err_msg':err_msg})
                else:
                    globals()['register'].password = password
                    comm_otp_generation()
                    return render(request,'templates_authentication/otp.html')

            else:
                err_msg = "Passwords doesn't match"
    
                return render(request,'templates_authentication/changepass.html',{'err_msg':err_msg})
           
        except ObjectDoesNotExist:
            err_msg = "Account doesn't exist"
        
            return render(request,'templates_authentication/changepass.html',{'err_msg':err_msg})

    else:
        return render(request,'templates_authentication/changepass.html')  


    
def comm_otp_generation():
    otp_rand =  random.randint(1000,9999)
    globals()['otp_global'] = otp_rand
    otp_msg = f"Email-Verification OTP : {otp_rand}"
    send_mail(
        "Welcome to ExaPro",
        otp_msg,
        'ExaPro<exapro.official@gmail.com>',
        [dec(globals()['email'])],
        fail_silently=False
    )

def show(request):
    return render(request,'templates_authentication/show.html')


def payment(request,prize):
    if request.method == 'POST':
            
        try:
           
            globals()['register'] = Register.objects.get(email = globals()['email'])
            date = datetime.datetime.now()
            date = date.strftime('%d-%m-%Y')
            date = str(date)
            d,m,y = date.split(sep='-')    
            m = int(m)
            y = int(y)

            month = int(request.POST['month'])
            year = int(request.POST['year'])

            if(month <= m and year<= y):
                return render(request,'templates_authentication/payment.html',{'err_msg':"Card expired",'prize':prize})
            else:
                payment = Payment(email=globals()['email'] ,prize=prize)
                payment.save()
                return render(request,'templates_authentication/payment.html',{'succ_msg':"Payment Successfull",'prize':prize})
        except  ObjectDoesNotExist:
            return render(request,'templates_authentication/payment.html',{'err_msg':"Signup up for payment",'prize':prize})

    else:
        return render(request,'templates_authentication/payment.html',{'prize':prize})

def dashboard(request):
    return render(request,'templates_website/dashboard.html')
