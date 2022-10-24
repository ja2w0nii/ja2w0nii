from django.shortcuts import render, redirect, get_object_or_404
from .models import UserModel
from django.contrib.auth import get_user_model #사용자가 있는지 검사하는 함수
from django.contrib import auth # 사용자 auth 기능
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.

#로그인
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        me = auth.authenticate(request, username=username, password=password)
        if me is not None:
            auth.login(request, me)
            return redirect('/')
        else:
            return redirect('/signin')

    elif request.method == 'GET':
        user = request.user.is_authenticated  # 사용자가 로그인 되어 있는지 검사
        if user:  # 로그인이 되어 있다면
            return redirect('/')
        else:  # 로그인이 되어 있지 않다면
            return render(request, 'user/account/signin.html')


#회원가입
def signup(request):

    if request.method == 'GET':
        user = request.user.is_authenticated # 로그인 된 사용자가 요청하는지 검사
        if user: # 로그인이 되어있다면
            return redirect('/')
        else: # 로그인이 되어있지 않다면
            return render(request, 'user/account/signup.html')

    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        bio = request.POST.get('bio', '')

        if password != password2:
            return render(request, 'user/account/signup.html', {'error': '패스워드가 다릅니다.'})
        else:
            if username == '' or password == '':
                return render(request, 'user/account/signup.html', {'error': '사용자 이름과 패스워드는 필수 입력 바랍니다.'})

            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'user/account/signup.html', {'error': '사용자 이름이 이미 존재합니다.'})
            else:
                UserModel.objects.create_user(username=username, password=password, bio=bio)
                return redirect('/signin')


#로그아웃
@login_required
def logout(request):
    auth.logout(request) # 인증 되어있는 정보를 없애기
    return redirect("/signin")


#유저 프로필
def profile(request, username):
    user = get_object_or_404(UserModel, username=username)
    context = {
        'user': user
    }
    return render(request, 'user/account/profile.html', context)