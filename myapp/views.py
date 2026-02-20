from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,Group
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect


# Create your views here.
from myapp.models import Complaint, Users, logs, Authority, Criminals, Police, Criminaldetection


def login_get(request):
    return render(request,"login.html")

def login_post(request):
    username=request.POST['username']
    password=request.POST['password']
    user=authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        if user.groups.filter(name="admin"):
            return redirect("/myapp/admin_home/")
        elif user.groups.filter(name="authority"):
            return redirect("/myapp/authority_home/")
        else:
            messages.error(request,'no such group')
            return redirect("/myapp/login_get/")
    else:
        messages.error(request, 'no such user found')
        return redirect("/myapp/login_get/")

def logout_get(request):
    logout(request)
    return redirect('/myapp/login_get/')


def forgotpassword_get(request):
    return render(request,'forgot_password.html')

def forgotpassword_post(request):
    return

#ADMIN...

def admin_home(request):
    return render(request,'admins/admin_home.html')

def add_authority_get(request):
    return render(request,'admins/add authority.html')

def add_authority_post(request):
    name=request.POST['name']
    email=request.POST['email']
    photo=request.FILES['photo']
    phone=request.POST['phone']
    place=request.POST['place']
    pin=request.POST['pincode']
    district=request.POST['district']
    state=request.POST['state']

    fs=FileSystemStorage()
    date=datetime.now().strftime('%d%M%Y%H%M%S')+".jpg"
    fs.save(date,photo)
    path=fs.url(date)

    u=User.objects.create_user(username=email,password=phone)
    u.groups.add(Group.objects.get(name="authority"))
    u.save()

    a=Authority()
    a.authorityname=name
    a.email=email
    a.photo=path
    a.phone=phone
    a.place=place
    a.pin=pin
    a.district=district
    a.state=state
    a.USER=u
    a.save()
    return redirect('/myapp/viewauthority_get/')


def add_police_get(request):
    return render(request,'admins/add_police.html')


def add_police_post(request):
    name = request.POST['name']
    email = request.POST['email']
    photo = request.FILES['photo']
    phoneno = request.POST['phoneno']
    post=request.POST['post']
    place = request.POST['place']
    pin = request.POST['pincode']

    fs = FileSystemStorage()
    date = datetime.now().strftime('%d%M%Y%H%M%S') + ".jpg"
    fs.save(date, photo)
    path = fs.url(date)

    u = User.objects.create_user(username=email, password=phoneno)
    u.groups.add(Group.objects.get(name="police"))
    u.save()

    a = Police()
    a.name = name
    a.email = email
    a.photo = path
    a.phoneno = phoneno
    a.post = post
    a.place = place
    a.pin = pin
    a.USER = u
    a.save()
    return redirect('/myapp/viewpolice_get/')


def viewpolice_get(request):
    a = Police.objects.all()
    return render(request,'admins/policeview.html',{'data':a})


def delete_police(request,id):
    Police.objects.get(USER=id).delete()
    return redirect('/myapp/viewpolice_get/')

def edit_police_get(request,id):
    data = Police.objects.get(id=id)
    return render(request,'admins/edit_police.html',{'data':data})

def edit_police_post(request):
    id=request.POST['id']
    name = request.POST['name']
    email = request.POST['email']
    phoneno = request.POST['phone']
    post = request.POST['post']
    place = request.POST['place']
    pin = request.POST['pincode']

    a = Police.objects.get(id=id)

    if 'photo' in request.FILES:
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        date = datetime.now().strftime('%d%M%Y%H%M%S') + ".jpg"
        fs.save(date, photo)
        path = fs.url(date)
        a.photo = path

    a.name = name
    a.email = email
    a.phone = phoneno
    a.post=post
    a.place = place
    a.pin = pin
    a.save()
    return redirect('/myapp/viewpolice_get/')

def admin_viewcriminaldetection_get(request):
    a=Criminaldetection.objects.all()
    return render(request,'admins/adminviewcriminaldetection.html',{'data':a})

def change_password_get(request):
    return render(request,'admins/change_password.html')

def change_password_post(request):
    current_pass = request.POST['currentpassword']
    new_pass = request.POST['newpassword']
    confirm_pass = request.POST['confirmpassword']

    data=request.user
    if  data.check_password(current_pass):
        if new_pass==confirm_pass:
            data.set_password(new_pass)
            data.save()
            return redirect("/myapp/login_get/")
        else:
            return redirect("/myapp/change_password_get/")
    else:
        return redirect("/myapp/change_password_get/")


def edit_authority_get(request,id):
    data=Authority.objects.get(id=id)
    return render(request,'admins/edit authority.html',{'data':data})

def edit_authority_post(request):
    id = request.POST['id']
    name = request.POST['name']
    email = request.POST['email']

    phone = request.POST['phone']
    place = request.POST['place']
    pin = request.POST['pincode']
    district = request.POST['district']
    state = request.POST['state']

    a = Authority.objects.get(id=id)

    b=a.AUTHUSER
    b.username=email
    b.save()
    a.authorityname = name
    a.email = email
    if 'photo' in request.FILES:
        photo = request.FILES['photo']

        fs = FileSystemStorage()
        date = datetime.now().strftime('%d%M%Y%H%M%S') + ".jpg"
        fs.save(date, photo)
        path = fs.url(date)
        a.photo = path
    a.phone = phone
    a.place = place
    a.pin = pin
    a.district = district
    a.state = state
    a.AUTHUSER=b
    a.save()
    return redirect('/myapp/viewauthority_get/')

def delete_authority(request,id):
    Authority.objects.get(AUTHUSER=id).delete()
    User.objects.get(id=id).delete()
    return redirect('/myapp/viewauthority_get/')

def sendreply_get(request,id):
    return render(request,'admins/sendreply.html',{'id':id})

def sendreply_post(request):
    id=request.POST['id']
    reply=request.POST['reply']
    data=Complaint.objects.get(id=id)
    data.reply=reply
    data.status="replied"
    data.save()
    return redirect('/myapp/viewcomplaint_get/')

def viewauthority_get(request):
    data = Authority.objects.all()
    return render(request,'admins/viewauthority.html',{'data':data})

def viewblockedusers_get(request):
    data=Users.objects.filter(status="blocked")
    return render(request,'admins/viewblockedusers.html',{'Users':data})

def viewcomplaint_get(request):
    data=Complaint.objects.all()
    return render(request,'admins/viewcomplaint.html',{'data':data})

def viewlogs_get(request):
    data=logs.objects.all()
    return render(request,'admins/viewlogs.html',{'logs':data})

def viewuser_get(request):
    data=Users.objects.all()
    return render(request,'admins/viewuser.html',{'Users':data})

def blockeduser(request,id):
    Users.objects.filter(id=id).update(status="blocked")
    return redirect('/myapp/viewblockedusers_get/')


#AUTHORITY...

def authority_home(request):
    return render(request,'Authority/authority_home.html')

def a_change_password_get(request):
    return render(request,'Authority/change_password.html')

def a_change_password_post(request):
    current_pass = request.POST['currentpassword']
    new_pass = request.POST['newpassword']
    confirm_pass = request.POST['confirmpassword']

    data=request.user
    if  data.check_password(current_pass):
        if new_pass==confirm_pass:
            data.set_password(new_pass)
            data.save()
            return redirect("/myapp/login_get/")
        else:
            return redirect("/myapp/a_change_password_get/")
    else:
        return redirect("/myapp/a_change_password_get/")

def viewprofile_get(request):
    data=Authority.objects.get(AUTHUSER=request.user)
    return render(request,'Authority/viewprofile.html',{'data':data})

def edit_profile_get(request):
    data=Authority.objects.get(AUTHUSER=request.user)
    return render(request,'Authority/edit_profile.html',{'data':data})

def edit_profile_post(request):
    id = request.POST['id']
    name = request.POST['name']
    email = request.POST['email']

    phone = request.POST['phone']
    place = request.POST['place']
    pin = request.POST['pincode']
    district = request.POST['district']
    state = request.POST['state']

    a = Authority.objects.get(id=id)

    b = a.AUTHUSER
    b.username = email
    b.save()
    a.authorityname = name
    a.email = email
    if 'photo' in request.FILES:
        photo = request.FILES['photo']

        fs = FileSystemStorage()
        date = datetime.now().strftime('%d%M%Y%H%M%S') + ".jpg"
        fs.save(date, photo)
        path = fs.url(date)
        a.photo = path
    a.phone = phone
    a.place = place
    a.pin = pin
    a.district = district
    a.state = state
    a.AUTHUSER = b
    a.save()

    return redirect('/myapp/viewprofile_get/')

def a_viewcomplaint_get(request):
    data=Complaint.objects.all()
    return render(request,'Authority/viewcomplaintpolice.html',{'data':data})

def a_sendreply_get(request,id):
    return render(request,'Authority/sendreplytopolice.html',{'id':id})

def a_sendreply_post(request):
    id=request.POST['id']
    reply=request.POST['reply']
    data=Complaint.objects.get(id=id)
    data.reply=reply
    data.status="replied"
    data.save()
    return redirect('/myapp/a_viewcomplaint_get/')


def manage_criminals_get(request):
    return render(request,'Authority/manage_criminals.html')

def manage_criminals_post(request):
    cname=request.POST['criminalname']
    photo=request.POST['photo']
    identification=request.POST['identification']
    dob=request.POST['dob']
    offense=request.POST['offense']
    height=request.POST['height']
    weight=request.POST['weight']
    gender=request.POST['gender']
    phone=request.POST['phoneno']

    fs = FileSystemStorage()
    date = datetime.now().strftime('%d%M%Y%H%M%S') + ".jpg"
    fs.save(date, photo)
    path = fs.url(date)

    c=Criminals()
    c.criminalname=cname
    c.photo=path
    c.identification=identification
    c.dob=dob
    c.offense=offense
    c.height=height
    c.weight=weight
    c.gender=gender
    c.phoneno=phone
    c.save()

    return redirect('/myapp/')

def viewcriminals_get(request):

    return render(request,'Authority/viewcriminals.html')

def register_authority_get(request):
    return render(request,'Authority/register_authority.html')

def register_authority_post(request):
    return

def sendcomplainttoadmin_get(request):
    return render(request,'Authority/sendcomplainttoadmin.html')

def sendcomplainttoadmin_post(request):
    return

def sendreplytopolice_get(request):
    return render(request,'Authority/sendreplytopolice.html')

def sendreplytopolice_post(request):
    return

def viewcomplaintpolice_get(request):
    data = Complaint.objects.all()
    return render(request, 'Authority/viewcomplaintpolice.html', {'data': data})


def viewcriminaldetection_get(request):
    return render(request,'Authority/viewcriminaldetection.html')



def viewobjectdetection_get(request):
    return render(request,'Authority/viewobjectdetection.html')

def viewpolicestaff_get(request):
    return render(request,'Authority/viewpolicestaff.html')



def viewreply_get(request):
    return render(request,'Authority/viewreply.html')


#POLICE...

def register_police_get(request):
    return render(request,'Police/register_police.html')

def register_police_post(request):
    return

def sendcomplaintpolice_get(request):
    return render(request,'Police/sendcomplaintpolice.html')

def sendcomplaintpolice_post(request):
    return

def viewcriminaldetectionpolice_get(request):
    return render(request,'Police/viewcriminaldetectionpolice.html')

def viewobjectdetectionpolice_get(request):
    return render(request,'Police/viewobjectdetectionpolice.html')

# def viewpolice_get(request):
#     return render(request,'Police/viewpolice.html')

def viewreplypolice_get(request):
    return render(request,'Police/viewreplypolice.html')

