from django.shortcuts import render, redirect
# user import
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
# models.Account
from datetime import date
from django.core.files.storage import FileSystemStorage
from .models import *




@csrf_exempt
def signup(request):
    if request.method == 'POST':
        print(request.method)
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(name,email,password)
        user = User(username = name, email=email, password=password)
        user.save()
        return redirect('/login_user/')


    return render(request, 'signup.html')


@csrf_exempt
def login_user(request):
    try:
        if request.method == 'POST':
            print(request.POST)
            name = request.POST.get('name')
            password = request.POST.get('password')
            if not name or not password:
                messages.success(
                    request, 'Both username and Password is Required')
                return redirect('/')

            user = authenticate(username=name, password=password)
            if user is None:
                messages.success(request, 'Wrong Password')
                return redirect('/')

            login(request, user)
            print('success')
            return redirect('/index/')
    except Exception as e:
        print('no')

    return render(request, 'login.html')



@login_required(login_url="login_user")
def index(request):
    current_user = request.user
    user_id = current_user.id
    print(user_id)
    return render(request, 'index.html' )


@login_required(login_url="login_user")
def donate(request ):
    try:
        data_fund = Raise_user.objects.all()
        return render(request, 'donate_page.html', {'fund': data_fund})
    except Exception as e:
        print('abscasc')






@login_required(login_url="login_user")
def about(request):
    return render(request, 'about.html')


def logout_user(request):
    logout(request)
    return redirect('/login_user/')


@login_required(login_url="login_user")
@csrf_exempt
def raise_exception(request ):
    if request.method == 'POST':
        uname = request.POST.get('name')
        uemail = request.POST.get('email')
        unumber = request.POST.get('number')
        ucause = request.POST.get('cause')
        file_up = request.FILES.get('file_up')
        udescription = request.POST.get('description')
        # print(name , email , number , cause , file , description)
        fs = FileSystemStorage()
        filename = fs.save(file_up.name, file_up)
        print(filename)
        file_url = fs.url(filename)
        print(file_url)
        time = date.today()
        Raise_user.objects.create(name=uname, email=uemail, date=time, number=unumber,
                                  cause=ucause, doc_file=file_url, cause_description=udescription)
        return redirect('index')

    return render(request, 'raise.html')


@login_required(login_url="login_user")
@csrf_exempt
def donate_form(request ,id ):
    add = Raise_user.objects.get(id = id)
    # print(add)
    if request.method == 'POST':
        print(request.method)
        # id = request.POST.get('id')
        print('mnas scmascans')
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        addres = request.POST.get('address')
        city = request.POST.get('city')
        card_name = request.POST.get('card_name')
        card_number = request.POST.get('card_number')
        amount = request.POST.get('amount')
        year = request.POST.get('year')
        cvv = request.POST.get('cvv')
        print('enter')
        user = Donate_fund.objects.create( donate_fund = add ,  full_name=fullname, email=email, address=addres,
                               city=city, name_on_card=card_name, card_number=card_number, amount=amount, exp_year=year, cvv=cvv)
        # user.save()
        return redirect('index')

    return render(request, 'donate.html')
