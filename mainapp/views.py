from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decoraters import allowed_users
from .models import Client, Staff
from .forms import ClientForm, StaffForm

# Create your views here.
def loginUser(request):
    if request.user.is_authenticated:
        return redirect("dashboard-staff")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect("dashboard-staff")

    return render(request, "login.html")

def logoutUser(request):
    logout(request)
    return redirect("login")

login_required(login_url="login")
@allowed_users(allowed=["admin"])
def dashboardStaff(request):
    form = StaffForm()
    if request.method == "POST":
        form = StaffForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("dashboard-staff")
    client = Client.objects.all()
    context = {"form":form, "client":client}
    return render(request, "dashboardstaff.html", context)


login_required(login_url="login")
def dashboardClient(request):
    form = ClientForm()
    if request.method == "POST":
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.member = request.user.member
            form.save()
            return redirect("dashboard-client")
    staff = Staff.objects.all()
    context = {"form":form, "staff":staff}
    return render(request, "dashboardclient.html",context)