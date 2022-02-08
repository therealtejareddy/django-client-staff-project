from django.contrib import admin
from .models import Client, Staff, Member
# Register your models here.
admin.site.register(Client)
admin.site.register(Staff)
admin.site.register(Member)
