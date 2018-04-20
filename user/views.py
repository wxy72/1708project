import hashlib

from django.http import HttpResponse
from django.shortcuts import render,redirect

from user.models import User

from user.forms import RegisterForm,Logingform

from django.contrib.auth import authenticate,login

from django.contrib.auth.hashers import make_password,check_password

# Create your views here.


def login_in(request):
	if request.method == 'POST':
		login_form = Logingform(request.POST)
		if login_form.is_valid():
			cd = login_form.cleaned_data
			user = authenticate(username=cd['username'],password=cd['password'])
			if user:
				login(request,user)
				return render(request,'info.html')
		else:return HttpResponse('msg wrong,try agin')
	return render(request,'login.html',{})

def register(request):
	form = 	RegisterForm(request.POST,request.FILES)
	if form.is_valid():
		user=form.save(commit=False)
		# user.password = make_password(user.password)
		user.password = password2MD5(user.password)
		user.save()
		request.session['uid'] = user.id
		request.session['nickname'] = user.nickname
		return redirect('/user/info/')
	return render(request,'register.html',{})


def info(request):
	uid = request.session.get('uid')
	if uid:
		user = User.objects.get(id=uid)
		return render(request,'info.html',{'user':user})
	return render(request,'login.html',{})

def loginout(request):
	request.session.flush()
	return render(request,'register.html')


def password2MD5(password):
	md5 = hashlib.md5()
	md5.update(password.encode('utf-8'))
	return md5.hexdigest()





