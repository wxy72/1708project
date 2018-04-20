from django.shortcuts import render,redirect

from user.models import User

from user.forms import RegisterForm

# Create your views here.


def login(request):
	return render(request,'login.html',{})

def register(request):
	form = 	RegisterForm(request.POST,request.FILES)
	if form.is_valid():
		user=form.save()
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