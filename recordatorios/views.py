from django.shortcuts import render
from django.urls import reverse_lazy
from recordatorios.models import Status, Priority, Reminder
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from recordatorios.forms import StatusForm, PriorityForm, ReminderForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q

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

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ListStatus(LoginRequiredMixin, ListView):
    model = Status

    def get_queryset(self):
        user = self.request.user
        if user:
            return Status.objects.filter(user=user)
        else:
            return Status.objects.all()

class UpdateStatus(LoginRequiredMixin, UpdateView):
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('status_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class DeleteStatus(LoginRequiredMixin, DeleteView):
    model = Status
    success_url = reverse_lazy('status_list')

##########################################################################################

class CreatePriority(LoginRequiredMixin, CreateView):
    form_class = PriorityForm
    template_name = 'recordatorios/priority_form.html'
    success_url = reverse_lazy('priority_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ListPriority(LoginRequiredMixin, ListView):
    model = Priority

    def get_queryset(self):
        user = self.request.user
        if user:
            return Priority.objects.filter(user=user)
        else:
            return Priority.objects.all()

class UpdatePriority(LoginRequiredMixin, UpdateView):
    model = Priority
    form_class = PriorityForm
    success_url = reverse_lazy('priority_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
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
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class ListReminder(LoginRequiredMixin, ListView):
    model = Reminder

    def get_queryset(self):
        user = self.request.user
        query = self.request.GET.get('q')
        status = self.request.GET.get('status', None)
        
        queryset = Reminder.objects.filter(user=user)
        
        if status:
            queryset = queryset.filter(status=status)
        
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
        
        return queryset.order_by('-priority')

class DetailReminder(LoginRequiredMixin, DetailView):
    model = Reminder

class UpdateReminder(LoginRequiredMixin, UpdateView):
    model = Reminder
    form_class = ReminderForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class DeleteReminder(LoginRequiredMixin, DeleteView):
    model = Reminder
    success_url = reverse_lazy('home')