from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout 
from .models import Room,Topic,Message,User, UserActivity
from .forms import RoomForm,UserForm,MyUserCreationForm
from datetime import timedelta
# Create your views here.

def home(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(Q(topic__name__icontains=q)|
        Q(name__icontains=q)|
        Q(description__icontains=q))
    total_rooms=rooms.count()    
    if total_rooms <10 and total_rooms >5: 
        room_messages=Message.objects.filter(Q(room__topic__name__icontains=q))[0: total_rooms ]
    else: 
        room_messages=Message.objects.filter(Q(room__topic__name__icontains=q))[0: 10]
    Topics=Topic.objects.all()[0:5]
    context = {'rooms': rooms,'topics':Topics, 'total_rooms':total_rooms,'room_messages':room_messages}

    return render(request, 'base/home.html', context)

def loginPage(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
            user=User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist.')

        user = authenticate(request,email=email,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Password does not exist.')

    context={'page':page}
    return render(request,'base/login_register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')    

def registerPage(request):
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,message='An error occuring during registration')
    return render(request,'base/login_register.html',{'form':form})

def room(request, pk):
    room = Room.objects.get(id=pk)
    room_messages= room.message_set.all().order_by('-created')
    participants = room.participants.all()
    if request.method=='POST':
        message=Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room',pk=room.id)
    context = {'room': room,'room_messages':room_messages,'participants':participants}
    
    return render(request, 'base/room.html', context)

def userProfile(request,pk):
    user=User.objects.get(id=pk)
    rooms=user.room_set.all()
    user.username=user.username
    room_messages=user.message_set.all()
    topics=Topic.objects.all()
    context={'user':user,'rooms':rooms,'room_messages':room_messages,'topics':topics}
    return render(request,'base/profile.html',context)

@login_required(login_url='login')
def createroom(request):
    form = RoomForm()
    topics=Topic.objects.all()
    if request.method == 'POST':
        topic_name=request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)

        Room.objects.create(
            host=request.user,
            topic=topic,
            name = request.POST.get('name'),
            description = request.POST.get('description')
           )
        return redirect('home')
    
    context = {'form': form,'topics':topics}
    return render(request, 'base/rooms_form.html', context)

@login_required(login_url='login')
def updateroom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    topics=Topic.objects.all()

    if request.user != room.host:
        return HttpResponse('You are not allowed here!!!')
    
    if request.method == 'POST':
        topic_name=request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        room.name = request.POST.get('name')
        room.topic=topic
        room.description= request.POST.get('description')
        room.save()
        return redirect('home')
    
    context = {'form': form,'topics':topics,'room':room}
    return render(request, 'base/rooms_form.html', context)

@login_required(login_url='login')
def deleteroom(request, pk):
    room = Room.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse('You are not allowed here!!!')

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    
    context = {'obj': room}
    return render(request, 'base/delete_room.html', context)

@login_required(login_url='login')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)
    if request.user != message.user:
        return HttpResponse('You are not allowed here!!!')

    if request.method == 'POST':
        message.delete()
        return redirect('home')
        # return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
    
    context = {'obj': message}
    return render(request, 'base/delete_room.html', context)

 
@login_required(login_url='login')
def updateUser(request):
    user=request.user
    form=UserForm(instance = user)
    
    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES , instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile',pk=user.id)
    return render(request, 'base/update_user.html',{'form':form})

def topicsPage(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.filter(name__icontains=q)
    return render(request, 'base/topics.html',{'topics':topics})

def activityPage(request):
    room_messages = Message.objects.all()[0:4]
    return render(request, 'base/activity.html',{'room_messages':room_messages})