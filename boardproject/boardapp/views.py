from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate,login,logout
from .models import BoardModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

def signupfunc(request):
    if request.method == "POST": #htmlファイルに入力されたものがPOSTの場合（formに入力されたとき）
        username = request.POST['username'] # formに入力された"username"を掴んでくる
        password = request.POST['password'] # formに入力された"password"を掴んでくる
        try: # ユーザー重複チェック
            user = User.objects.create_user(username,'','password') # ←コマンドによってユーザーが作成される。引数(username,e-mail,password)
            return render(request, 'signup.html',{'some':100})
        except IntegrityError: # ユーザーが重複し、かつ「IntegrityError」が発生した場合に実行
            return render(request, 'signup.html',{'error':'このユーザーはすでに登録されていますこのユーザーはすでに登録されています。'})
    return render(request,'signup.html') # renderはHTTPレスポンスオブジェクトをする作成する。GETの場合はサインアップ画面表示

def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password) # 対象ユーザーが存在するかどうか認証する（また権限確認） 
        if user is not None: # userが存在する場合
            login(request, user)
            return redirect('list') # 「urls.pyファイル」でしたnameと一致したURL先に遷移する。
        else:                # userが存在しない場合
            return render(request, 'login.html',{'context':'ログイン失敗'})
        pass
    return render(request, 'login.html',{}) # GETメソッド

@login_required #ログイン状態の判定
def listfunc(request):
    object_list = BoardModel.objects.all() # BoardModelにある全オブジェクトをobjece_list変数に入れる。
    return render(request, 'list.html',{'object_list':object_list}) # ←htmlファイルで「object_list」を使用できるようになる。

def logoutfunc(request):
    logout(request)
    return redirect('login')

def detailfunc(request,pk):
    object = get_object_or_404(BoardModel,pk=pk)
    return render(request,'detail.html',{'object':object})

def goodfunc(reques,pk):
    object = BoardModel.objects.get(pk=pk)
    object.good = object.good + 1
    object.save()
    return redirect('list')

def readfunc(request,pk):
    object = BoardModel.objects.get(pk=pk)
    username = request.user.get_username() # ログインユーザーのusername情報をとってくる
    if username in object.readtext: # 既にいいねを押している場合
        return redirect('list')
    else: # いいねを押していない場合
        object.read = object.read + 1
        object.readtext = object.readtext + ' ' + username
        object.save()
        return redirect('list')
    
class BoardCreate(CreateView):
    template_name = 'create.html'
    model = BoardModel
    fields = ('title','content','author','snsimage')
    success_url = reverse_lazy('list')