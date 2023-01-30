from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib import messages
from .forms import SignupForm,LoginForm,ImageUploadForm,UpdateForm,ChangePasswordForm
from .models import Signup1,Image1
# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST or none,request.FILES or None)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            photo=form.cleaned_data['Photo']
            confirm=form.cleaned_data['ConfirmPassword']

            user=Signup1.objects.filter(Email=email).exists()

            if user:
                messages.warning(request, "Email Already Exixts")
                return redirect('/signup')
            elif password!=confirm:
                messages.warning(request, "Mismatch")
                return redirect('/signup')
            else:
                tab=Signup1(Name=name,Age=age,Photo=photo,Email=email,Password=password)
                tab.save()
                messages.success(request, "Signup Succesfully")
                return redirect('/')
    else:
        form=SignupForm()
    return render(request, 'signup.html',{'form':form})

def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            
            try:
                user=Signup1.objects.get(Email=email)

                if not user:
                    messages.warning(request, "Email doesnot Exists")
                    return redirect('/login')
                elif password!=user.Password:
                    messages.warning(request, "Incorrect")
                    return redirect('/login')
                else:
                    messages.success(request, "Login succesfully")
                    return redirect('/home/%s' % user.id)
            except:
                messages.warning(request, "Email or Password incorrect ")
                return redirect('/signup')
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})


def home(request,id):
    data=Signup1.objects.get(id=id)
    return render(request, 'home.html',{'data':data})


def gallery(request):
    users=Image1.objects.all()
    return render(request,'gallery.html',{'users':users})
    
def details(request,id):
    user=Image1.objects.get(id=id)
    return render(request,'details.html',{'user':user})


def update(request,id):
    updt=Signup1.objects.get(id=id)
    if request.method=='POST':
        form=UpdateForm(request.POST or None,instance=updt)
        if form.is_valid():
            form.save()
            messages.success(request, "Update Successfully")
            return redirect('/')
    else:
        form=UpdateForm(instance=updt)
    return render(request, 'update.html',{'updt':updt,'form':form})

def changepassword(request,id):
    delt=Signup1.objects.get(id=id)
    if request.method=='POST':
        form=ChangePasswordForm(request.POST)
        if form.is_valid():
            old=form.cleaned_data['OldPassword']
            new=form.cleaned_data['NewPassword']
            confirm=form.cleaned_data['ConfirmPassword']

            if old!=delt.Password:
                messages.warning(request, "Incorrect Password")
                return redirect('/changepassword/%s' % delt.id)
            elif old==new:
                messages.warning(request, "Same Password")
                return redirect('/changepassword/%s' % delt.id)
            elif new!=confirm:
                messages.warning(request,"Mismatch")
                return redirect('/changepassword/%s' % delt.id)
            else:
                delt.Password=new
                delt.save()
                messages.success(request, "Password Changed")
                return redirect('/home/%s' % delt.id)
    else:
        form=ChangePasswordForm()
    return render(request,'password.html',{'delt':delt,'form':form})


def logouts(request):
    logout(request)
    messages.success(request,"Logout Successfully")
    return redirect('/')