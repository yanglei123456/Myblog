from django.shortcuts import render,redirect
from myblogs.models import Post_messages
from myblogs.models import User_messages
from django.http import HttpResponse
from django.utils import timezone
from django.db import models
#第一种办法
#定义name判断网页是否有cook name信息
def name(request):
    if 'username'in request.COOKIES:
        username = request.COOKIES['username']
    else:
         username =  ''
    return username
def mima(request):
    if 'password'in request.COOKIES:
        password = request.COOKIES['password']
    else:
         password =  ""
    return password 
#定义登录判断装饰器：
def login_decorate(view_func):
    def wrapper(request,*args,**kwargs):
        if 'username'in request.COOKIES:
            username = request.COOKIES['username']
            #说明此时登录啦 跳转到要访问的页面上：
            return view_func(request,*args,**kwargs)
        else:
            return redirect(request,*args,**kwargs)
    return wrapper

def index(request):
    posts = Post_messages.objects.all()
    return render(request,'myblogs/index.html',{'posts':posts,'username':name(request)})

def login(request):
    #调用name和mima方法来传递username和password
    return render(request,'myblogs/login.html',{'username':name(request),'password':mima(request)})

def login_check(request):
#    return render(request,'myblogs/login.html')
    user_name = request.POST.get('username')
    pass_word = request.POST.get('password')
    on_or_off = request.POST.get('cookie_on_or_off')
    print(on_or_off)
#    if user_name == 'yanglei' and pass_word == '123456':
    a = User_messages.objects.get(name=user_name,password=pass_word)
    if len(str(a))!=0:

        response = redirect('/index')
        if on_or_off == 'on':
            #如果是on则记住用户名
            response.set_cookie('username',user_name,max_age=2*12*60*60)
            response.set_cookie('password',pass_word,max_age=2*12*60*60)
        return response
    else:
        return redirect('/login')




def detail(request,num):
    m =Post_messages.objects.get(id=num)
    return render(request,'myblogs/detail.html',{'m':m})

@login_decorate
def create(request):
    #user_name = request.POST.get('username')
    user_name = request.COOKIES['username']
   # pass_word = request.POST.get('password')
  #  pass_word = request.COOKIES['password']
   # print(user_name)
    return render(request,'myblogs/create.html',{'user_name':user_name})

def create_contention(request):
 #用于将提交的新的博客内容存放于数据库
    user_name = request.COOKIES['username']
    pass_word = request.COOKIES['password']
    title = request.POST.get('title')
    slug = request.POST.get('slug')
    body = request.POST.get('body')
    a = User_messages.objects.get(name=user_name,password=pass_word)
    
    b = Post_messages()
    b.title = title
    b.slug = slug
    b.body = body
    b.username_id = a.id
    b.save()
    return redirect('index.html')

def register2(request):
    #注册用户数据保存到数据库
    username = request.POST.get('username')
    password = request.POST.get('password')
    date = request.POST.get('date')
    qq = request.POST.get('qq')
    c = User_messages()
    c.name = username
    c.password = password
    c.qq = qq 
    c.register_date = date
    c.save()
    #return HttpResponse(username)
    return redirect('index.html')
    
def register(request):
    #注册页面
    return render(request,'myblogs/register.html')
@login_decorate
def center(request,username):
    a = User_messages.objects.get(name=username)
    b = a.post_messages_set.all()
    #由一类查询多类 一类的对象.多累名小写_set(),获取说有的多累对象

    #bs = Post_messages.objects.filter(username_id=a.id)
    return render(request,"myblogs/center.html",{"b":b})

def logout(request):
#            response.set_cookie('username',user_name,max_age=2*12*60*60)
   # return render(request,'myblogs/index.html',{"username":None})
    return redirect('/index.html')
