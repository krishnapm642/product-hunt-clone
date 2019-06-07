from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
	if request.method == "POST":
		#all the details entered and redy to create account
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.get(username = request.POST['username'])
				return render(request, 'accounts/signup.html',{'error':'Username already exist'})

			except User.DoesNotExist:
				user = User.objects.create_user(username =  request.POST['username'],password = request.POST['password1'])
				auth.login(request, user)
				return redirect('home')
		else:
			return render(request, 'accounts/signup.html',{'error':'Passwords are not matching'})
	else:
		#here the signup page will show
		return render(request, 'accounts/signup.html')

def login(request):
	if request.method == "POST":
		user = auth.authenticate(username = request.POST['username'], password = request.POST['password'])
		if user is not None:
			auth.login(request, user)
			return redirect('home')
		else:
			return render(request, 'accounts/login.html',{'error':'username and passwords are incorrect'})
	else:
		return render(request, 'accounts/login.html')


def logout(request):
	if request.method == "POST":
		auth.logout(request)
		return redirect('home')
