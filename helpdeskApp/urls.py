from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tickets/', views.ticketList, name='ticketList'),
    path('my-tickets/', views.userTickets, name='userTickets'),
    path('add-ticket/', views.addTicket, name='addTicket'),
    path('sign-up/', views.signUp, name='signUp'),
    path('log-in/', views.logIn, name='logIn'),
    path('logout/', views.logoutUser, name='logoutUser'),
    path('tickets/detail/<int:pk>/', views.ticketDetails, name='ticketDetails'),
]