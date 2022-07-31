from django.shortcuts import render, redirect, get_object_or_404
from .models import Department, Ticket
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import UserRegistrationForm, AddTicketForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


def home(request):
    return render(request, "site/home.html")

#staff vision
def ticketList(request):
    departments = Department.objects.all()
    tickets = Ticket.objects.all().order_by('-ticketDate')
    return render(request, "site/tickets.html", {
        'departments': departments,
        'tickets': tickets
    })

def ticketDetails(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == "POST":
        ticket.isActive = False
        ticket.save()
        return redirect('userTickets')
    return render(request, "site/ticket-detail.html", {
        'ticket': ticket
    })

def userTickets(request):
    user = request.user
    userTickets = Ticket.objects.filter(user=user).order_by('-ticketDate')
    return render(request, "site/user-tickets.html", {
        'user': user,
        'userTickets': userTickets
    })

def addTicket(request):
    form = AddTicketForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            newTicket = form.save(commit=False)
            newTicket.user = request.user
            newTicket.save()
            form.save_m2m()
            return redirect('userTickets')
    return render(request, "site/add-ticket.html", {
        'form': form
    })


def signUp(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('logIn')
    else:
        form = UserRegistrationForm()

    return render(request, "user/sign-up.html", {
        'form': form
    })


def logIn(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "user/login.html", {
        "form": form
    })


def logoutUser(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("home")