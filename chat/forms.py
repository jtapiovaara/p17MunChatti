from django import forms
from django.contrib.auth.admin import Group, User

ROOMS = Group.objects.all()


class RoomName(forms.Form):
    room_name = forms.ChoiceField(choices=ROOMS)
