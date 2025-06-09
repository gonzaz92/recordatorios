from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from recordatorios.models import Status, Priority, Reminder
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from recordatorios.forms import StatusForm, PriorityForm, ReminderForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Max
from django.db import transaction

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
        max_orden = Status.objects.filter(user=self.request.user).aggregate(Max('orden'))['orden__max'] or 0
        form.instance.orden = max_orden + 1
        return super().form_valid(form)
    
def up_status(request, pk):
    status = get_object_or_404(Status, pk=pk, user=request.user)
    with transaction.atomic():
        previous = Status.objects.filter(user=request.user, orden__lt=status.orden).order_by('-orden').first()
        if previous:
            status.orden, previous.orden = previous.orden, status.orden
            status.save()
            previous.save()
        return redirect('status_list')

def down_status(request, pk):
    status = get_object_or_404(Status, pk=pk, user=request.user)
    with transaction.atomic():
        next = Status.objects.filter(user=request.user, orden__gt=status.orden).order_by('orden').first()
        if next:
            status.orden, next.orden = next.orden, status.orden
            status.save()
            next.save()
        return redirect('status_list')

class ListStatus(LoginRequiredMixin, ListView):
    model = Status

    def get_queryset(self):
        return Status.objects.filter(user=self.request.user).order_by('orden')

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
        max_orden = Priority.objects.filter(user=self.request.user).aggregate(Max('orden'))['orden__max'] or 0
        form.instance.orden = max_orden + 1
        return super().form_valid(form)
    
def up_priority(request, pk):
    priority = get_object_or_404(Priority, pk=pk, user=request.user)
    with transaction.atomic():
        previous = Priority.objects.filter(user=request.user, orden__lt=priority.orden).order_by('-orden').first()
        if previous:
            priority.orden, previous.orden = previous.orden, priority.orden
            priority.save()
            previous.save()
    return redirect('priority_list')

def down_priority(request, pk):
    priority = get_object_or_404(Priority, pk=pk, user=request.user)
    with transaction.atomic():
        next = Priority.objects.filter(user=request.user, orden__gt=priority.orden).order_by('orden').first()
        if next:
            priority.orden, next.orden = next.orden, priority.orden
            priority.save()
            next.save()
    return redirect('priority_list')

class ListPriority(LoginRequiredMixin, ListView):
    model = Priority

    def get_queryset(self):
        return Priority.objects.filter(user=self.request.user).order_by('orden')

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
        
        return queryset.order_by('priority')

class DetailReminder(LoginRequiredMixin, DetailView):
    model = Reminder

class UpdateReminder(LoginRequiredMixin, UpdateView):
    model = Reminder
    form_class = ReminderForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def get_success_url(self):
        return reverse_lazy('reminder_detail', kwargs={'pk': self.object.pk})

class DeleteReminder(LoginRequiredMixin, DeleteView):
    model = Reminder
    success_url = reverse_lazy('home')