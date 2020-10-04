from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.views import generic
from .models import Blog
from django.urls import reverse
from .forms import BlogForm, LoginForm, RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
    else:
        return render(request, "blogsite/register.html")

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
        else:
            messages.info(request, "Invalid credentials")
            return redirect('/blogsite/login/')

        return redirect('/blogsite/blogs/')
    else:
        return render(request, 'blogsite/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/blogsite/blogs/')

def create(request, user_id):
    if request.method == 'POST':
        q=User.objects.get(id=user_id)
        b=request.POST['blog']
        q.blog.create(blog_text=b)
        return redirect('/blogsite/blogs/')
    else:
        return render(request, 'blogsite/create.html')

def update(request, user_id):
    if request.method == 'POST':
        q=User.objects.get(id=user_id)
        r=User.objects.get(id=user_id)
        q.password=request.POST['password1']
        q.username=request.POST['username']
        q.first_name=request.POST['first_name']
        q.last_name=request.POST['last_name']
        q.email=request.POST['email']
        if q.password == request.POST['password2']:
            if User.objects.filter(username=q.username).exists() and r.username!=q.username:
                messages.info(request,"Username Taken")
                return redirect('/blogsite/' + str(user_id) + '/update/')
            elif User.objects.filter(email=q.email).exists() and r.email!=q.email:
                messages.info(request,"Email Taken")
                return redirect('/blogsite/' + str(user_id) + '/update/')
            else:
                q.save()
                return redirect('/blogsite/blogs/')
        else:
            messages.info(request,"Passwords not matching")
            return redirect('/blogsite/' + str(user_id) + '/update/')
        
    else:
        return render(request, 'blogsite/update.html')

        

class Blogview(generic.ListView):
    template_name='blogsite/blogs.html'
    context_object_name='blogs_list'

    def get_queryset(self):
        return Blog.objects.all()

# class Editview(generic.DetailView):
#     model = Blog
#     template_name='blogsite/edit.html'

def edit(request, blog_id):
    current_user=request.user
    q=Blog.objects.get(id=blog_id)
    if current_user.id==q.user.id:
        if request.method=="POST":
            q=Blog.objects.get(id=blog_id)
            q.blog_text=request.POST['blog']
            q.save()
            return redirect('/blogsite/blogs/')
        else:
            return render(request, 'blogsite/edit.html', {'Blog':q})
    else:
        messages.info(request, "You are not authorised to access this blog")
        return redirect('/blogsite/blogs/')

def deleteblog(request, blog_id):
    if request.method=="POST":
        q=Blog.objects.get(id=blog_id)
        q.delete()
        return redirect('/blogsite/blogs/')
    else:
        return render(request, 'blogsite/deleteblog.html')

def deleteuser(request, user_id):
    if request.method=="POST":
        q=User.objects.get(id=user_id)
        q.delete()
        return redirect('/blogsite/blogs/')
    else:
        return render(request, 'blogsite/deleteuser.html')