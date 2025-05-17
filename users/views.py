from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from users.forms import UserForm, ChangePasswordForm, UserUpdateForm
from django.urls import reverse_lazy

##########################################################################################

class UserSignUp(CreateView):
    form_class = UserForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

class UserDetail(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'registration/user_detail.html'

class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    form_class= UserUpdateForm
    template_name = 'registration/signup.html'
    
    def get_success_url(self):
        return reverse_lazy('user_detail', kwargs={'pk': self.object.pk})

class UserDelete(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'registration/user_confirm_delete.html'
    success_url = reverse_lazy('login')

class UserLogin(LoginView):
    next_page = reverse_lazy('home')

class UserLogout(LogoutView):
    next_page = reverse_lazy('login')

class ChangePassword(LoginRequiredMixin, PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('home')