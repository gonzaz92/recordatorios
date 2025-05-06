from recordatorios.models import Status, Priority, Reminder
from itertools import groupby

def list_status(request):
    if request.user.is_authenticated:
        list_status = Status.objects.filter(user=request.user).values('id', 'name')
    else:
        list_status = []
    return {'list_status': list_status}

def list_priority(request):
    if request.user.is_authenticated:
        list_priority = Priority.objects.filter(user=request.user).values('id', 'name', 'color')
    else:
        list_priority = []
    return {'list_priority': list_priority}

# def list_reminder(request):
#     list_reminder = Reminder.objects.values('id', 'title', 'status', 'priority').order_by('-priority')
#     return {'list_reminder': list_reminder}

def list_reminder(request):
    if not request.user.is_authenticated:
        return {'list_reminder': []}
    else:
        # Obtener los recordatorios ordenados por priority
        list_reminder = list(Reminder.objects.filter(user=request.user).values('id', 'title', 'status', 'priority','user').order_by('-priority'))

        # Agrupar por 'status'
        grouped_by_status = groupby(sorted(list_reminder, key=lambda x: x['status']), key=lambda x: x['status'])

        # Filtrar los primeros 7 elementos de cada grupo
        filtered_reminders = []
        for status, group in grouped_by_status:
            filtered_reminders.extend(list(group)[:7])

        return {'list_reminder': filtered_reminders}