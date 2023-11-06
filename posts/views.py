from asyncio import selector_events
from pickletools import read_uint1
from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def index(request):
    posts = Post.objects.all()
    users = User.objects.all()

    dropDownData ={

    }    
    return render(request, 'index.html', {'posts':posts, 'users':users})

def create(request):
    if request.user.is_authenticated:
        users = User.objects.all()
        if request.method == 'POST':
            title = request.POST['title']
            body = request.POST['body']
            selectedAuthor = request.POST['selectedAuthor']
            author = User.objects.get(username=selectedAuthor)
            # authorID = authorUsername.id
            # author = User.objects.get(id=authorID)
            post_image = request.FILES['post_image']

            post = Post.objects.create(title=title, body=body, author=author, post_image=post_image)
            post.save()
            return redirect('/')
            # if User.objects.filter(username=selectedAuthor).exists():
            #     author = User.objects.filter(username=selectedAuthor).first()
            #     post = Post.objects.create(title=title, body=body, author=author)
            #     post.save()
            #     return redirect('/')
            # else:
            #     messages.info(request, 'User ' + selectedAuthor + ' does not exist')
            #     return redirect('/create')
            

        else:
            return render(request, 'create.html', {'users':users})
    else:
        # messages.info(request, 'You need to login to create a post')
        return redirect('login')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials. Ole!')
            return redirect('login')

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
    
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exsists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password does not match')
            return redirect('register')

    else:
        return render(request, 'register.html')

def postAuthor(request, pk, name):
    # name = request.user.username
    # author = User.objects.get(username=name)
    posts = Post.objects.all().filter(author__exact=pk)
    user = User.objects.get(id=pk)
    name = user.username

    author_data = {
        'posts':posts,
        'name':name
    }
    return render(request, 'postAuthor.html', {'author_data':author_data})

def viewPost(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'viewPost.html', {'post':post})

def edit_post(request, pk):
    post = Post.objects.get(id=pk)
    users = User.objects.all()

    if request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        selectedAuthor = request.POST['selectedAuthor']
        author = User.objects.get(username=selectedAuthor)

        post.title = title
        post.body = body
        post.author = author
        post.save()
        return redirect('/')
    return render(request, 'editPost.html', {'post':post, 'users':users})
    
def search(request):
    if request.method == "POST":
        search_term = request.POST['search_bar']

        posts = Post.objects.filter(body__contains=search_term)

        return render(request, 'search.html', {'posts':posts, 'search_term':search_term})
    else:
        return render(request, 'index.html')



def profile(request, name):
    if request.user.is_authenticated:
        pk = request.user.id
        posts = Post.objects.all().filter(author__exact=pk)
        # user = User.objects.get(id=pk)
        # name = user.username

        author_data = {
            'posts':posts,
            'name':name
        }
    
        return render(request, "profile.html", {'author_data':author_data})
    
    return redirect("login")



def delete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect("/")


def edit_profile(request, pk):
    profile = User.objects.get(id=pk)

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        # password = request.POST['password']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']

        profile.username = username
        profile.email = email
        profile.first_name = firstname
        profile.last_name = lastname
        profile.save()
        return redirect("/profile/{{request.user.username}}")

    return render(request, 'editRegister.html', {'profile':profile})