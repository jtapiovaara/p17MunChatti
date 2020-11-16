from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.admin import Group, User
from django.conf import settings
from django.contrib.auth.decorators import login_required
from chat.forms import RoomName


def logout(request):
    logout(request)
    # return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

@login_required
def index(request):
    rooms = Group.objects.all()
    context = {
        'rooms': rooms
    }
    return render(request, 'chat/index.html', context)


def room(request, room_name):
    name = room_name
    members = User.objects.filter(groups__name__exact=name).select_related()
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'members': members
    })
