from django.shortcuts import render, redirect
from .forms import TicketForm
from .models import Ticketinfo
from django.views.generic import ListView, DetailView, UpdateView
'''
# Create your views here.
class Member_list(ListView):
    model = gym
    template_name = 'list.html'

class Member_register(UpdateView):
    model = gym
    template_name = 'register.html' '''


def passenger_list(request):
    context = {'passenger_list': Ticketinfo.objects.all()}
    return render(request, "list.html", context)


def bookticket(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = TicketForm()
        else:
            passenger = Ticketinfo.objects.get(pk=id)
            form = TicketForm(instance=passenger)
        return render(request, "register.html", {'form': form})
    else:
        if id == 0:
            form = TicketForm(request.POST)
        else:
            passenger = Ticketinfo.objects.get(pk=id)
            form = TicketForm(request.POST, instance=passenger)
        if form.is_valid():
            form.save()
        return redirect('/list/')


def passenger_delete(request, id):
    passenger = Ticketinfo.objects.get(pk=id)
    passenger.delete()
    return redirect('/list/')
