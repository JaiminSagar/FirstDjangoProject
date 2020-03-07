from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from first_app.models import Topic,Webpage,AccessRecord,User_Model
from . import forms # or from first_app import forms
from first_app.forms import NewUserModelForm, UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.he
def index(request):
    # return HttpResponse("<em>First App</em>")
    # my_dic = {'insert_me': "Hello I am from views.py from first_app!"}
    # return render(request, 'index.html', context=my_dic)

    # webpages_list = AccessRecord.objects.order_by('date')
    # date_dict = {'access_records': webpages_list}
    my_dic = {'insert_me': "Hello I am coming from templates/first_app_temp/index.html"}
    return render(request, 'first_app_temp/index.html', context=my_dic)

def display(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'first_app_temp/display_record.html', context=date_dict)

def display_users(request):
    usr_list = User_Model.objects.all()
    user_dict = {'access_records': usr_list}
    return render(request, 'first_app_temp/display_users.html', context=user_dict)

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Validation Success.....")
            print("Name: " + form.cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print("Text: " + form.cleaned_data['text'])

    return render(request, 'first_app_temp/form_page.html', {'form': form})

def sign_up(request):
    form = NewUserModelForm()

    if request.method == "POST":
        form = NewUserModelForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FROM INVALID")

    return render(request, 'first_app_temp/sign_up.html', {'form':form})

def register(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        print(fname,lname,email)
        register_user = User_Model()
        register_user.FirstName = fname
        register_user.LastName = lname
        register_user.Email = email
        register_user.save()
        print("Data saved sucessfully..........")
        return redirect("/first_app/display_users/")
    return render(request, "first_app_temp/Register.html", {})

def navbar(request):
    return render(request, "first_app_temp/base.html", {})


def user_registration(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'first_app_temp/user_registration_temp.html',
                  {
                      'user_form': user_form,
                      'profile_form': profile_form,
                      'registered': registered
                  })


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request,user)
                print("User is Active")
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not Active")
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password: {}".format(username,password))
            return HttpResponse("invalid login details supplied")
    else:
        return render(request, "first_app_temp/user_login.html", {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are logged in.....Yeh")