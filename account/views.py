from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm
from django.views.generic import UpdateView
from .models import User


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            message = messages.success(request, f"User {username} has been created successfully")
            return redirect("votes:index")
    else:
        form = UserRegisterForm()
    return render(request, 'account/register.html', {"form": form})


@login_required
def profile(request):
    return render(request, "account/profile.html")


class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    fields = ["first_name", "last_name", "email", "profile_img", "widgets"]
    success_url = reverse_lazy("votes:index")


# class RegisterView(View):
#     def get(self, request):
#         form = UserRegister
#         return render(request, 'account/register.html', {"form": form})
#
#     def post(self, request):
#         form = UserRegister(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             form.save()
#             message = messages.success(request, f"User {username} created successfully")
#             return redirect("home")
#         return render(request, 'account/register.html', {"form": form})
