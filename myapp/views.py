from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.shortcuts import render, redirect


# Create your views here.
from myapp.models import Complaint, Users, logs, Authority, Criminals, Police, Criminaldetection, Objectdetection


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

@login_required(login_url="/myapp/login_get/")
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
    a.AUTHUSER=u
    a.save()
    return redirect('/myapp/viewauthority_get/')

@login_required(login_url="/myapp/login_get/")
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

@login_required(login_url="/myapp/login_get/")
def viewpolice_get(request):
    a = Police.objects.all()
    return render(request,'admins/policeview.html',{'data':a})


def delete_police(request,id):
    Police.objects.get(USER=id).delete()
    return redirect('/myapp/viewpolice_get/')

@login_required(login_url="/myapp/login_get/")
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

@login_required(login_url="/myapp/login_get/")
def admin_viewcriminaldetection_get(request):
    a=Criminaldetection.objects.all()
    return render(request,'admins/adminviewcriminaldetection.html',{'data':a})

@login_required(login_url="/myapp/login_get/")
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

@login_required(login_url="/myapp/login_get/")
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

@login_required(login_url="/myapp/login_get/")
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

@login_required(login_url="/myapp/login_get/")
def viewauthority_get(request):
    data = Authority.objects.all()
    return render(request,'admins/viewauthority.html',{'data':data})

@login_required(login_url="/myapp/login_get/")
def viewblockedusers_get(request):
    data=Users.objects.filter(status="blocked")
    return render(request,'admins/viewblockedusers.html',{'Users':data})

@login_required(login_url="/myapp/login_get/")
def viewcomplaint_get(request):
    data=Complaint.objects.all()
    return render(request,'admins/viewcomplaint.html',{'data':data})

@login_required(login_url="/myapp/login_get/")
def viewlogs_get(request):
    data=Objectdetection.objects.all().order_by('-id')
    return render(request,'admins/viewlogs.html',{'data':data})

@login_required(login_url="/myapp/login_get/")
def viewuser_get(request):
    data=Users.objects.all()
    return render(request,'admins/viewuser.html',{'Users':data})

def blockeduser(request,id):
    Users.objects.filter(id=id).update(status="blocked")
    return redirect('/myapp/viewblockedusers_get/')


#AUTHORITY...

def authority_home(request):
    return render(request,'Authority/authority_home.html')

@login_required(login_url="/myapp/login_get/")
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

@login_required(login_url="/myapp/login_get/")
def viewprofile_get(request):
    data=Authority.objects.get(AUTHUSER=request.user)
    return render(request,'Authority/viewprofile.html',{'data':data})

@login_required(login_url="/myapp/login_get/")
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

@login_required(login_url="/myapp/login_get/")
def manage_criminals_get(request):
    return render(request,'Authority/manage_criminals.html')

def manage_criminals_post(request):
    cname=request.POST['criminalname']
    photo=request.FILES['photo']
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

    return redirect('/myapp/viewcriminals_get/')

@login_required(login_url="/myapp/login_get/")
def viewcriminals_get(request):
    data=Criminals.objects.all()
    return render(request,'Authority/viewcriminals.html',{'data':data})

@login_required(login_url="/myapp/login_get/")
def edit_criminal_get(request,id):
    data=Criminals.objects.get(id=id)
    return render(request,'Authority/edit_criminals.html',{'data':data})

def edit_criminal_post(request):
    id=request.POST['id']
    cname=request.POST['criminalname']
    photo=request.POST.get('photo')
    identification=request.POST['identification']
    dob=request.POST['dob']
    offense=request.POST['offense']
    height=request.POST['height']
    weight = request.POST['weight']
    gender = request.POST['gender']
    phone = request.POST['phoneno']

    c = Criminals.objects.get(id=id)

    # photo optional
    if 'photo' in request.FILES:
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        date = datetime.now().strftime('%d%M%Y%H%M%S') + ".jpg"
        fs.save(date, photo)
        path = fs.url(date)
        c.photo = path
    c.criminalname = cname
    c.identification = identification
    c.dob = dob
    c.offense = offense
    c.height = height
    c.weight = weight
    c.gender = gender
    c.phoneno = phone
    c.save()
    return redirect('/myapp/viewcriminals_get/')

def delete_criminal(request,id):
    Criminals.objects.filter(id=id).delete()
    return redirect('/myapp/viewcriminals_get/')

@login_required(login_url="/myapp/login_get/")
def register_authority_get(request):
    return render(request,'Authority/register_authority.html')

def register_authority_post(request):
    return

@login_required(login_url="/myapp/login_get/")
def sendcomplainttoadmin_get(request):
    return render(request,'Authority/sendcomplainttoadmin.html')

def sendcomplainttoadmin_post(request):
    complaint=request.POST['complaint']
    from datetime import datetime
    c=Complaint()
    c.date=datetime.now().date()
    c.complaint=complaint
    c.reply="pending"
    c.status="pending"
    c.AUTHUSER=User.objects.get(id=request.user.id)
    c.save()
    return redirect('/myapp/viewreply_get/')

@login_required(login_url="/myapp/login_get/")
def sendreplytopolice_get(request,id):
    return render(request,'Authority/sendreplytopolice.html',{'id':id})

def sendreplytopolice_post(request):
    id = request.POST['id']
    reply = request.POST['reply']
    data = Complaint.objects.get(id=id)
    data.reply = reply
    data.status = "replied"
    data.save()
    return redirect('/myapp/viewcomplaintpolice_get/')
    return

@login_required(login_url="/myapp/login_get/")
def viewcomplaintpolice_get(request):
    data = Complaint.objects.all()
    l=[]
    for i in data:
        if Police.objects.filter(USER_id=i.AUTHUSER.id).exists():
            name=Police.objects.get(USER_id=i.AUTHUSER.id).name
            l.append({
                'id':i.id,
                'date':i.date,
                'complaint':i.complaint,
                'reply':i.reply,
                'status':i.status,
                'name':name
            })

    return render(request, 'Authority/viewcomplaintpolice.html', {'data': l})

@login_required(login_url="/myapp/login_get/")
def viewcriminaldetection_get(request):
    return render(request,'Authority/viewcriminaldetection.html')


@login_required(login_url="/myapp/login_get/")
def viewobjectdetection_get(request):
    return render(request,'Authority/viewobjectdetection.html')

@login_required(login_url="/myapp/login_get/")
def viewpolicestaff_get(request):
    data=Police.objects.all()
    return render(request,'Authority/viewpolicestaff.html',{'data':data})

@login_required(login_url="/myapp/login_get/")
def viewreply_get(request):
    data=Complaint.objects.filter(AUTHUSER=request.user.id)
    return render(request,'Authority/viewreply.html',{'data':data})


#POLICE...

def register_police_get(request):
    return render(request,'Police/register_police.html')

def register_police_post(request):
    return

@login_required(login_url="/myapp/login_get/")
def sendcomplaintpolice_get(request):
    return render(request,'Police/sendcomplaintpolice.html')

def sendcomplaintpolice_post(request):
    return

@login_required(login_url="/myapp/login_get/")
def viewcriminaldetectionpolice_get(request):
    return render(request,'Police/viewcriminaldetectionpolice.html')

@login_required(login_url="/myapp/login_get/")
def viewobjectdetectionpolice_get(request):
    return render(request,'Police/viewobjectdetectionpolice.html')

# def viewpolice_get(request):
#     return render(request,'Police/viewpolice.html')

@login_required(login_url="/myapp/login_get/")
def viewreplypolice_get(request):
    return render(request,'Police/viewreplypolice.html')



#App

def app_login_post(request):
    username=request.POST['username']
    password=request.POST['password']
    user=authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        print(request.POST,"============")
        if user.groups.filter(name="police"):
            return JsonResponse({'status':'ok','lid':str(user.id)})
        else:
            return JsonResponse({'status':'no'})
    else:
        return JsonResponse({'status':'no'})

def app_view_profile(request):
    lid=request.POST['lid']
    data=Police.objects.get(USER_id=lid)
    return JsonResponse({'status':'ok','name':data.name,'email':data.email,
                         'photo':data.photo,'phoneno':data.phoneno,'post':data.post,
                         'place':data.place,'pin':data.pin})


def app_change_password_post(request):
    current_pass = request.POST['currentpassword']
    new_pass = request.POST['newpassword']
    confirm_pass = request.POST['confirmpassword']
    lid=request.POST['lid']
    # data=Police.objects.get(USER_id=lid)
    data=User.objects.get(id=lid)
    if data.check_password(current_pass):
        if new_pass==confirm_pass:
            data.set_password(new_pass)
            data.save()
            return JsonResponse({'status':'ok'})
        else:
            return JsonResponse({'status':'no'})
    else:
        return JsonResponse({'status':'no'})


def app_sendcomplaint_post(request):
    lid=request.POST['lid']
    complaint=request.POST['complaint']
    from datetime import datetime
    c=Complaint()
    c.date=datetime.now().date()
    c.complaint=complaint
    c.reply="pending"
    c.status="pending"
    c.AUTHUSER=User.objects.get(id=lid)
    c.save()
    return JsonResponse({'status':'ok'})


def app_viewreply_get(request):
    lid=request.POST['lid']
    data=Complaint.objects.filter(AUTHUSER=lid)
    l=[]
    for i in data:
        l.append({'id':i.id,'date':i.date,'complaint':i.complaint,'reply':i.reply,'status':i.status})
    return JsonResponse({'status':'ok','data':l})

def app_viewobjectdetectionpolice_get(request):
    a=Objectdetection.objects.all()
    list=[]
    for i in a:
        list.append({
            'id':i.id,
            'log':i.log,
            'place':i.place,
            'time':i.time,
            'date':i.date
            # 'photo':i.photo
        })
    return JsonResponse({'status':'ok','data':list})

def app_viewcriminaldetectionpolice_get(request):
    a = Criminaldetection.objects.all()
    list = []
    for i in a:
        list.append({
            'id': i.id,
            'date': i.date,
            'photo': i.photo,
            'time': i.time
            # 'photo':i.photo
        })
    return JsonResponse({'status': 'ok', 'data': list})


# u=User.objects.get(username='admin')
# u.set_password('123456')
# u.save()


# @csrf_exempt
def and_criminal_view_noti(request):
    nid=request.POST['nid']
    print(nid)
    from datetime import datetime,timedelta
    # today = datetime.now().date()  # Today's date
    # two_days_later = today + timedelta(days=2)
    # print(two_days_later)
    dd=Criminaldetection.objects.filter(id__gt=nid,date=datetime.now().date()).order_by('id')
    if dd.exists():
        f=dd[0]
        print(f.id)
        # return JsonResponse({"status":"ok",'nid':f.id,'message':"Prisoner detected on camera: "+f.PRISONER.name })
        return JsonResponse({"status":"ok",'nid':f.id,'message':f.CRIMINAL.criminalname +" detected on camera"})
    else:
        return JsonResponse({"status": "no"})