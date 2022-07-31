from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Department, Ticket


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label="First name", max_length=101)
    last_name = forms.CharField(label="Last name", max_length=101)
    email = forms.EmailField(label="E-mail")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class AddTicketForm(forms.ModelForm):
    problemDescription = forms.CharField(label="Problem description", widget=forms.Textarea)
    department = forms.ModelChoiceField(label='Choice department', queryset=Department.objects.all())
    photo = forms.ImageField(required=False)
    class Meta:
        model = Ticket
        fields = ['problemDescription', 'department', 'photo']