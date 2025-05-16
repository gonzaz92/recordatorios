from django import forms
from recordatorios.models import Status, Priority, Reminder
from ckeditor.widgets import CKEditorWidget

##########################################################################################

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Extraemos 'user' si está en kwargs
        super().__init__(*args, **kwargs)
        if user:
            self.instance.user = user 

class PriorityForm(forms.ModelForm):
    class Meta:
        model = Priority
        fields = ['name', 'color']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'type': 'color'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Extraemos 'user' si está en kwargs
        super().__init__(*args, **kwargs)
        if user:
            self.instance.user = user 

class ReminderForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Reminder
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['status'].queryset = Status.objects.filter(user=user)
            self.fields['priority'].queryset = Priority.objects.filter(user=user)