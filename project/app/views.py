from django.shortcuts import render, redirect
from .forms import LoginForm, UserForm
from .models import CustomUser
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def signin(request):
        if request.method == "POST":
                form = LoginForm(request.POST)
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(username = username, password = password)

                if user is not None:
                        login(request, user)
                        return redirect('index')
                else:
                        return HttpResponse('로그인 실패, 다시 시도 해보세요.')
        else:
                form = LoginForm()
                return render(request, 'app/signin.html', {'form':form})

def signup(request):
        if request.method == "POST":
                form = UserForm(request.POST)
                if form.is_valid():
                        new_user = CustomUser.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['email'], password=form.cleaned_data['password'], grade=form.cleaned_data['grade'], phone_number=form.cleaned_data['phone_number'])
                        login(request, new_user)
                        return redirect('index')
        else:
                form = UserForm()
                return render(request, 'app/signup.html', {'form':form})