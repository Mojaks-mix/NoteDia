from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Room,Topic,Message,User
from .forms import RoomForm,RoomFormMedia,CreateUserForm,UserForm,captchaForm,TopicForm
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


def Home(request):
    q=request.GET.get('q') 

    if request.GET.get('q') != None :
        rooms=Room.objects.filter(Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q)).order_by('-isProfessor','-rating_average','-created')
    else:
        q=''
        rooms=Room.objects.filter(Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q))

    room_count= rooms.count()

    if request.user.is_authenticated:
        topics=User.objects.get(id=request.user.id)

    else:
        topics =Topic.objects.all()[0:5]
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))


    context={'rooms':rooms,'room_count':room_count, 'room_messages':room_messages,'topics':topics}
    return render(request,'base/home.html',context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all()
    participants = room.participants.all()

    total_ratings = room.rating_count
    average_rating = room.rating_average

    if request.method == 'POST':
        rating_value = int(request.POST.get('rating', 0))
        message_body = request.POST.get('body')

        if message_body:
            message = Message.objects.create(
                user=request.user,
                room=room,
                body=message_body
            )
            room.participants.add(request.user)

        if 1 <= rating_value <= 5:
            if request.user == room.last_rated_by:  # Check if the same user is updating the rating
                room.rating_sum -= room.rating
            else:
                room.rating_count += 1

            room.rating_sum += rating_value
            room.rating = rating_value
            room.rating_average = room.rating_sum / room.rating_count
            room.last_rated_by = request.user
            room.save()

        return redirect('room', pk=room.id)

    context = {
        'room': room,
        'room_messages': room_messages,
        'participants': participants,
        'average_rating': average_rating,
        'total_ratings': total_ratings
    }
    return render(request, 'base/room.html', context)

def userProfile(request,pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()
    context={'user': user, 'rooms': rooms, 'room_messages':room_messages,'topics':topics}
    return render(request, 'base/profile.html', context)


@login_required(login_url='login')
def createRoom(request):
    page='create-room'
    form= RoomForm(data=request.POST)
    topics = Topic.objects.all()
    user=User.objects.get(id=request.user.id)
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created =Topic.objects.get_or_create(name = topic_name)

        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            isProfessor=user.isProfessor
        )
        return redirect('home')

    context ={'form': form, 'topics': topics,"page":page}
    return render(request,'base/room_form.html',context)


@login_required(login_url='login')
def createRoomMedia(request):
    page='create-room-media'
    form= RoomFormMedia(data=request.POST,files=request.FILES)
    user=User.objects.get(id=request.user.id)
    topics = Topic.objects.all()
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created =Topic.objects.get_or_create(name = topic_name)

        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            media_file = request.FILES['media_file'],
            isProfessor=user.isProfessor
        )
        return redirect('home')

    context ={'form': form, 'topics': topics,"page":page}
    return render(request,'base/room_form.html',context)


@login_required(login_url='login')
def updateRoom(request,pk):
    page = 'create-room-media'
    room=Room.objects.get(id=pk) 
    form=RoomFormMedia(request.POST,request.FILES,instance=room)
    topics = Topic.objects.all()

    if request.user != room.host:
        return HttpResponse('You are not allowed here!')

    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created =Topic.objects.get_or_create(name = topic_name)
        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')

        if request.FILES.get('media_file') != None: 
            room.media_file = request.FILES['media_file']

        room.save()
        return redirect('home')
    context={'form':form, 'topics': topics, 'room': room,'page': page}
    return render(request,'base/room_form.html',context)

@login_required(login_url='login')
def deleteRoom(request,pk):
    room=Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse('You are not allowed here!')

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request,'base/delete.html',{'obj':room})


@login_required(login_url='login')
def deleteMessage(request,pk):
    message=Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse('You are not allowed here!')

    if request.method == 'POST':
        message.delete()
        return redirect('room', pk=message.room.id)
    return render(request,'base/delete.html',{'obj':message})


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        captcha = captchaForm(request.POST)

        if not captcha.is_valid():
            messages.error(request, 'Invalid Captcha')
            return redirect('login')
        
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except ObjectDoesNotExist:
            messages.error(request, 'Username or password is incorrect')
            return redirect('login')

        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect')
            return redirect('login')

    context = {"page": page, "captcha": captchaForm}
    return render(request, 'base/login_register.html', context)



def registerPage(request):
    page='register'
    form=CreateUserForm()
    
    if request.method == 'POST':
        captcha = captchaForm(request.POST)

        if not captcha.is_valid():
            messages.error(request, 'Invalid Captcha')
            return redirect('register')
        
        form=CreateUserForm(request.POST)

        if form.is_valid(): 
            
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            login(request,user)
            return redirect('user-topics')
        else:
            messages.error(request,'Oops!! Something went wrong')
        
    context={'page':page,
             'form':form,
             'captcha':captchaForm
            }
    return render (request,"base/login_register.html",context)


@login_required(login_url='login')
def choose_topics(request):
    user=User.objects.get(id=request.user.id)
    user_major = user.major
    topics = Topic.objects.filter(majors__contains=user_major)
    if request.method == 'POST':
        user.topic.clear()
        choosen_topics=request.POST.getlist('topics')
        user.topic.set(choosen_topics)
        user.save()
        return redirect('home')


    context = {'topics': topics, 'user_major': user_major}
    return render(request, 'base/add_topics.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def updateUser(request):
    user=request.user

    form=UserForm(instance=user)
    

    if request.method == 'POST':
        form=UserForm(request.POST,request.FILES,instance=user)
        
        if form.is_valid():
            form.save()
            return redirect('user-profile',pk=user.id)
    return render(request,'base/update-user.html',{'form':form})

def topicsPage(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''
    topics=Topic.objects.filter(name__icontains=q)
    return render(request,'base/topics.html',{'topics':topics})

def activityPage(request):
    room_messages = Message.objects.all()
    return render(request,'base/activity.html',{'room_messages':room_messages})


@login_required(login_url='login')
def createTopic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save()
            messages.success(request, 'Topic added successfully.')
            return redirect('create-topic')
    else:
        form = TopicForm()
    
    context = {'form': form}
    return render(request, 'base/create_topic.html', context)


def UserResetPassword(request,pk):
    user = User.objects.get(id=pk)
    if request.user == user:
        if request.method == 'POST':
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1 == '' and password2 == '':
                messages.error(request, 'Please fill both fields')
                return redirect('reset-password', pk=pk)
            if password1 == password2:
                user.set_password(password1)
                user.save()
                return redirect('home')
            else:
                messages.error(request, 'Passwords do not match')
                return redirect('reset-password', pk=pk)
    else:
        messages.error(request, 'Something went wrong')
        return redirect('reset-password', pk=pk)

    return render(request,'base/reset-password.html') 