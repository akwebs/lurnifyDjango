from django.http import HttpResponse
from django.shortcuts import render , redirect
from courses.models import *
from django.contrib import messages
from django.forms import inlineformset_factory,modelformset_factory
from .forms import *
from django.contrib.auth import login, authenticate ,logout as deauth
import random
import requests

from django.contrib.auth.decorators import login_required


@login_required(login_url='members:member-login')
def member_home(request):
    try:
        if lurnify_member.objects.filter(account_id_id=request.user.id).exists():
            get_member=lurnify_member.objects.get(account_id_id=request.user.id)
            get_ref=referal_code.objects.get(lurnify_member_id=get_member)
            context={
                'member':get_member,
                'ref':get_ref,

            }
            return render(request , 'home/index.html',context)
        else:
            deauth(request)
            return redirect('members:member-login') 
    except Exception as e:
        print(e)
        return redirect('members:member-login')        


def send_otp(mobile , otp):
    print(mobile,otp)
    url= f"https://prpsms.co.in/API/SendMsg.aspx?uname=20190332&pass=itc@123&send=BCPLHO&dest={mobile}&msg=Dear Applicant, {otp} is your verification code for Online Application at Bansal Classes.%0A %0ATeam Bansal" 
    resp=requests.get(url)
    return None

def check_member_phone(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        reg_phone = request.POST.get('reg_phone')
        if phone:
            if not len(phone) == 10:
                return HttpResponse("<div id='username-error' class='error text-danger'>Please Enter 10 Digit Number</div>")
            if lurnify_member.objects.filter(phone=phone).exists():
                otp=str(random.randint(1000 , 9999))
                request.session['otp'] = otp
                request.session['phone'] = phone
                send_otp(phone , otp)
                return HttpResponse("""<div id='username-error'>
                                                <p>An OTP Has been sent to you</p>
                                                <input type='text' name="otp" class='form-control' placeholder='Enter OTP' 
                                                hx-post="/check_member_otp/" 
                                                hx-target="#otp-error" 
                                                hx-trigger="keyup delay:2s"
                                                />
                                        </div>""")
            else:
                return HttpResponse("<div id='username-error' class='error text-danger'>You are not Lurnify member</div>")
        if reg_phone:
            if not len(reg_phone) == 10:
                return HttpResponse("<div id='username-error' class='error text-danger'>Please Enter 10 Digit Number</div>")
            if Account.objects.filter(phone=reg_phone).exists():
                return HttpResponse("<div id='phone-error' class='error text-danger'>Phone number already exists</div>")
            else:
                otp=str(random.randint(1000 , 9999))
                request.session['reg_otp'] = otp
                send_otp(reg_phone , otp)
                return HttpResponse("""
                        <div id='phone-error'>
                            <p class='success text-success'>Phone number is available</p>
                            <input type='text' name="reg_otp" class='form-control' placeholder='Enter OTP' 
                            hx-post="/check_member_otp/"
                            hx-target="#otp-error"
                            hx-trigger="keyup delay:2s"
                            />
                        </div>""")    

def check_member_otp(request):
    try:
        if request.method == 'POST':
            otp = request.POST.get('otp')
            reg_otp= request.POST.get('reg_otp')

            if otp:
                session_otp = request.session.get('otp')
                if otp == session_otp:
                    return HttpResponse("<div id='otp-error' class='success text-success'>OTP is correct</div>")
                else:
                    return HttpResponse("<div id='otp-error' class='error text-danger'>OTP is incorrect</div>")
            if reg_otp:
                session_reg__otp = request.session.get('reg_otp')
                if reg_otp == session_reg__otp:
                    return HttpResponse("<div id='otp-error' class='success text-success'>OTP is correct</div>")
                else:
                    return HttpResponse("<div id='otp-error' class='error text-danger'>OTP is incorrect</div>")    
    except Exception as e:
        return HttpResponse("<div id='otp-error' class='error text-danger'>Something wennt wrong contact to Admin</div>")            

def login_view(request):
    if request.user.is_authenticated:
        return redirect('members:member-home')
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":

        if form.is_valid():
            phone = request.POST.get('phone')
            otp   = request.POST.get('otp')
            session_otp = request.session.get('otp')

            if lurnify_member.objects.filter(phone=phone).exists():
                if otp == session_otp:
                    user = Account.objects.get(phone=phone)
                    login(request, user)
                    return redirect('members:member-home')
            else:
                msg = "You are not Lurnify member"        
            
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})

def register(request):
    if request.user.is_authenticated:
        return redirect('members:member-home')
    if request.method == 'POST':
        phone = request.POST.get('reg_phone')
        otp   = request.POST.get('reg_otp')
        session_otp = request.session.get('reg_otp')
        name= request.POST.get('name')
        type= request.POST.get('type')
        address= request.POST.get('address')

        if not  len(phone) == 10:
            return HttpResponse("<div id='all-error' class='error text-danger'>Please Enter 10 Digit Number</div>")
        if  Account.objects.filter(phone=phone).exists():
            return HttpResponse("<div id='all-error' class='error text-danger'>No already Exist</div>") 
        if not  otp == session_otp:
            return HttpResponse("<div id='all-error' class='error text-danger'>OTP is incorrect</div>")
        if type == 'select':
            return HttpResponse("<div id='all-error' class='error text-danger'>Please Select type</div>")

        get_pass=Account.objects.create(phone=phone,username=name)    
        get_pass.set_password(get_pass.password)
        get_pass.save()

        member_obj=lurnify_member.objects.create(
            account_id=get_pass,
            phone=phone,
            name=name,
            member_type=member_type.objects.get(type_name=type),                   
            address=address,
        )
        if referal_code.objects.last():
            get_last= referal_code.objects.last()
            number=int(get_last.qr_code_number)+1
        else:
            number=100000
        referal_code.objects.create(
            lurnify_member_id = member_obj,
            qr_code_number=str(number),
        )
        login(request, get_pass)
        return redirect('members:member-home')
    context={
        'members':member_type.objects.all(),
    }
    return render(request, "accounts/register.html", context)
    
    
def get_fields(request):
    member_type = request.GET.get('type')
    print(member_type)
    
    if member_type == 'select':
        return HttpResponse("<div id='user_type' class='error text-danger'>Please Select type</div>")      
    
    if member_type == 'Driver':
        fields = 'Driver'
    else:
       fields='Others'
    return render(request, "accounts/partials/type.html", {"fields": fields})

def logout(request):
    deauth(request)
    return redirect('members:member-login')

def profile(request):
    pass