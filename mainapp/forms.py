from dataclasses import field
from django.forms import ModelForm
from .models import Client, Staff

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        exclude = ['member']

class StaffForm(ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'