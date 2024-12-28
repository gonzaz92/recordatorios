from django import forms
from recordatorios.models import Status, Priority, Reminder
from ckeditor.widgets import CKEditorWidget

##########################################################################################

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PriorityForm(forms.ModelForm):
    class Meta:
        model = Priority
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'type': 'color'}),
        }

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