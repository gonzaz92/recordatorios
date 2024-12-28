from django.shortcuts import render
from django.urls import reverse_lazy
from recordatorios.models import Status, Priority, Reminder
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from recordatorios.forms import StatusForm, PriorityForm, ReminderForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

##########################################################################################

@login_required
def home(request):
    return render(request, 'recordatorios/home.html')

@login_required
def cards(request):
    return render(request, 'recordatorios/cards.html')

##########################################################################################

class CreateStatus(LoginRequiredMixin, CreateView):
    form_class = StatusForm
    template_name = 'recordatorios/status_form.html'
    success_url = reverse_lazy('status_list')

class ListStatus(LoginRequiredMixin, ListView):
    model = Status

class UpdateStatus(LoginRequiredMixin, UpdateView):
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('status_list')

class DeleteStatus(LoginRequiredMixin, DeleteView):
    model = Status
    success_url = reverse_lazy('status_list')

##########################################################################################

class CreatePriority(LoginRequiredMixin, CreateView):
    form_class = PriorityForm
    template_name = 'recordatorios/priority_form.html'
    success_url = reverse_lazy('priority_list')

class ListPriority(LoginRequiredMixin, ListView):
    model = Priority

class UpdatePriority(LoginRequiredMixin, UpdateView):
    model = Priority
    form_class = PriorityForm
    success_url = reverse_lazy('priority_list')

class DeletePriority(LoginRequiredMixin, DeleteView):
    model = Priority
    success_url = reverse_lazy('priority_list')

##########################################################################################

class CreateReminder(LoginRequiredMixin, CreateView):
    form_class = ReminderForm
    template_name = 'recordatorios/reminder_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ListReminder(LoginRequiredMixin, ListView):
    model = Reminder

    def get_queryset(self):
        status = self.request.GET.get('status', None)
        user = self.request.user
        if status:
            return Reminder.objects.filter(user=user).filter(status=status).order_by('-priority')
        else:
            return Reminder.objects.all().order_by('-priority')

class DetailReminder(LoginRequiredMixin, DetailView):
    model = Reminder

class UpdateReminder(LoginRequiredMixin, UpdateView):
    model = Reminder
    form_class = ReminderForm
    success_url = reverse_lazy('home')

class DeleteReminder(LoginRequiredMixin, DeleteView):
    model = Reminder
    success_url = reverse_lazy('home')