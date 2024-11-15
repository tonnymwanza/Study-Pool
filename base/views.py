from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from .models import Room, Topic, Message, User
from django.views import View
from .forms import RoomForm, UserForm, MyUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views import View
from . models import Room

# Create your views here.

#the login login view

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            else:
                return redirect('home')
        else:
            messages.error(request, "Invalid username or password. Try again!!!")
            return redirect("login")
    return render(request, 'base/login.html')

#the logout view

def logoutUser(request):
    logout(request)
    return redirect('home')

#user registration view

def register(request):
    if request.method == "POST":
        firstname = request.POST["firstname"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "the username already exists. Use a different one!!!")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "the email is taken. Try another one!!!")
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=firstname, username=username, email=email, password=password2)                
                return redirect('login')
        else:
            messages.error(request, "the passwords do not match. Try again!!!")
            return redirect('register')
    return render(request, 'base/register.html')

#the view to render the homepage

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )[0:3]

    topics = Topic.objects.all()[0:5]
    all_rooms = Room.objects.all().count()
    room_count = rooms.count()
    room_messages = Message.objects.filter(
        Q(room__topic__name__icontains=q))[0:4]

    context = {'rooms': rooms, 'topics': topics,
               'room_count': room_count, 'room_messages': room_messages,
               "all_rooms": all_rooms}
    return render(request, 'base/home.html', context)

#the room view to display room  content

@login_required(login_url='login')
def room(request, pk):
    room = Room.objects.get(id=pk)
    total_likes = room.like.count()
    current_user = request.user
    count_followers = room.follow.count()
    room_follower = room.follow.all()
    room_messages = room.message_set.all()
    participants = room.participants.all()

    is_member = room.participants.filter(id=current_user.id).exists()

    if request.method == 'POST':
        if 'join' in request.POST:  # Logic for joining the room
            room.participants.add(current_user)
            return redirect('room', pk=room.id)
        elif 'message' in request.POST:  # Logic for sending a message
            if is_member:  # Only allow members to send messages
                Message.objects.create(
                    user=current_user,
                    room=room,
                    body=request.POST.get('body')
                )
                return redirect('room', pk=room.id)
            else:
                return redirect('room', pk=room.id)

    context = {'room': room, 'room_messages': room_messages,'total_likes': total_likes,
               'participants': participants, 'count_followers': count_followers, 'is_member': is_member}
    return render(request, 'base/room.html', context)

#the profile view, class based

class ProfileView(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request, pk):
        room_ = Room.objects.get(id=pk)
        room_host = room_.host
        user = User.objects.get(id=pk)
        total_user_followers = user.follower.count()
        rooms = user.room_set.all()
        room_messages = user.message_set.all()
        topics = Topic.objects.all()
        context = {
            'user': user,
            'rooms': rooms,
            'room_messages': room_messages,
            'topics': topics,
            'total_user_followers': total_user_followers,
            'room': room
        }
        return render(request, 'base/profile.html', context)
    
    def post(self, request, pk):
        user = User.objects.get(id=pk)
        room = Room.objects.get(id=pk)
        current_user = request.user
        if current_user in room.host.follower.all():
            room.host.follower.remove(current_user)
        else:
            room.host.follower.add(current_user)
            room.save()
        rooms = user.room_set.all()
        room_messages = user.message_set.all()
        topics = Topic.objects.all()
        context = {
            'user': user,
            'rooms': rooms,
            'room_messages': room_messages,
            'topics': topics,
            'room': room
        }
        return render(request, 'base/profile.html', context)

#the view to create a room

@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    topics = Topic.objects.all()
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)

        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            rules=request.POST.get('rules')
        )
        return redirect('home')

    context = {'form': form, 'topics': topics}
    return render(request, 'base/room_form.html', context)

#the view to update a room

@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    topics = Topic.objects.all()
    if request.user != room.host:
        return HttpResponse('Your are not allowed here!!')

    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()
        return redirect('home')

    context = {'form': form, 'topics': topics, 'room': room}
    return render(request, 'base/room_form.html', context)

#the view to delete a room

@login_required(login_url='login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse('Your are not allowed here!!')

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete_room.html', {'obj': room})

#the view of deleting room messages

@login_required(login_url='login')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)                                               

    if request.user != message.user:
        return HttpResponse('You cant delete the message!!')

    if request.method == 'POST':
        message.delete()
        return redirect('room', pk=pk)
    return render(request, 'base/delete.html', {'obj': message})

#the view of updating user profile

@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile', pk=user.id)

    return render(request, 'base/update-user.html', {'form': form})

#the view to render topics

@login_required(login_url='login')
def topicsPage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.filter(name__icontains=q)
    return render(request, 'base/topics.html', {'topics': topics})

@login_required(login_url='login')
def activityPage(request):
    room_messages = Message.objects.all()
    return render(request, 'base/activity.html', {'room_messages': room_messages})

def footer_page(request):
    return render(request, 'base/footer_page.html')

#the view following or unfollowing rooms

@login_required(login_url='login')
def follow_func(request, pk):
    room = Room.objects.get(id=pk)
    current_user = request.user
    count_followers = room.follow.count()
    room_follower = room.follow.all()
    if current_user in room.follow.all():
        room.follow.remove(current_user)
        room.save()
    else:
        room.follow.add(current_user)
        room.save()

    context = {
        'room': room,
        'count_followers': count_followers,
        'room_follower': room_follower
    }
    return redirect('room', pk=pk)

# the view to follow or unfollow users

def follow_user_view(request, pk):
    room = Room.objects.get(id=pk)
    user = User.objects.get(id=pk)
    current_user = request.user
    total_user_followers = room.host.follower.count()
    print(total_user_followers)
    if current_user in room.host.follower.all():
        room.host.follower.remove(current_user)
    else:
        room.host.follower.add(current_user)
        room.save()
    context = {
        'total_user_followers': total_user_followers,
        'user': user,
        'room': room
    }
    return redirect('profile', pk=pk)

#the view to like or dislike users

@login_required(login_url='login')
def user_likes(request, pk):
    room = Room.objects.get(id=pk)
    current_user = request.user
    
    if current_user in room.like.all():
        room.like.remove(current_user)
        room.save()
    else:
        room.like.add(current_user)
        room.save()
    context = {
        'room': room,
    }
    return redirect('room', pk=pk) 


