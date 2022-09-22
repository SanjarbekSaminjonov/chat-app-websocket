from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Room


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


@login_required
def index_view(request):
    return render(request, 'index.html', {
        'rooms': Room.objects.all(),
    })


@login_required
def room_view(request, room_name):
    chat_room, created = Room.objects.get_or_create(name=room_name)
    chat_room.join(request.user)
    return render(request, 'room.html', {
        'room': chat_room,
    })
