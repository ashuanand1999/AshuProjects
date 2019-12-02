from django.shortcuts import render, redirect
from .models import RegistrationData, FeedbackData
from .forms import RegistrationForm, FeedbackForm,LoginForm
from django.http import HttpResponse

import datetime as dt
date1 = dt.datetime.now()

def home_view(request):
    return render(request,'home.html')

def service_view(request):
    return render(request,'services.html')


def reg_view(request):
    if request.method == "POST":
        rform = RegistrationForm(request.POST)
        if rform.is_valid():
            fname = request.POST.get('fname', '')
            lname = request.POST.get('lname', '')
            user_name = request.POST.get('uname', '')
            passwd1 = request.POST.get('password1', '')
            passwd2 = request.POST.get('password2', '')
            mob = request.POST.get('mobile', '')
            email = request.POST.get('email', '')
            age = request.POST.get('age', '')
            gender = rform.cleaned_data.get('gender', '')
            no_marr = rform.cleaned_data.get('No_of_marriages', '')
            exp1 = rform.cleaned_data.get('Expectation1', '')
            exp2 = rform.cleaned_data.get('Expectation2', '')
            alc_st = rform.cleaned_data.get('alcoholic_status', '')
            more = rform.cleaned_data.get('more_info', '')

            data = RegistrationData(
                fname=fname,
                lname=lname,
                username=user_name,
                password1=passwd1,
                password2=passwd2,
                mobile=mob,
                email=email,
                gender=gender,
                age=age,
                No_of_marriages=no_marr,
                Expectation1=exp1,
                Expectation2=exp2,
                alcoholic_status=alc_st,
                more_info=more
            )
            data.save()
            rform = RegistrationForm()
            return render(request, 'registrationform.html', {'rform': rform})
        else:
            resp = "Please give the proper data."
            return HttpResponse(resp)
    else:
        rform = RegistrationForm()
        return render(request,'registrationform.html',{'rform': rform})

def userdata_view(request):
    uform = RegistrationData.objects.all()
    return render(request,'Userdata.html',{'usrform': uform})

def login_view(request):
    if request.method == "POST":
        lform = LoginForm(request.POST)
        if lform.is_valid():
            uname = request.POST.get('username', '')
            passwrd = request.POST.get('password', '')
            uname1 = RegistrationData.objects.filter(username=uname)
            passd = RegistrationData.objects.filter(password1=passwrd)
            if uname1 and passd:
                # def userdata_view(request):
                #     uform = RegistrationData.objects.all()
                #     return render(request,'Userdata.html',{'usrform': uform})
                return redirect(userdata_view)
            else:
                return HttpResponse('Username Does not exists.')
        else:
            return HttpResponse('Please give the data to all fields.')
    else:
        lform = LoginForm()
        return render(request,'loginform.html',{'lform': lform})

def feedback_view(request):
    if request.method == "POST":
        fform = FeedbackForm(request.POST)
        if fform.is_valid():
            fname = request.POST.get('fname', '')
            lname = request.POST.get('lname', '')
            mob = request.POST.get('mobile', '')
            email = request.POST.get('email', '')
            rate = request.POST.get('rating', '')
            feed = request.POST.get('feedback', '')
            fname = fname.title()
            lname = lname.title()
            data = FeedbackData(
                fname=fname,
                lname=lname,
                mobile=mob,
                email=email,
                rating=rate,
                feedback=feed,
                date=date1
            )
            data.save()
            fform = FeedbackForm()
            return render(request,'feedbackform.html',{'fform': fform})
        else:
            return HttpResponse('Please give the data to all fields.')
    else:
        fform = FeedbackForm()
        return render(request, 'feedbackform.html', {'fform': fform})

def gallery_view(request):
    return render(request,'gallery.html')


