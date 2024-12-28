from django.urls import path
from recordatorios.views import (home, cards,
                                CreateStatus, ListStatus, UpdateStatus, DeleteStatus,
                                CreatePriority, ListPriority, UpdatePriority, DeletePriority,
                                CreateReminder, ListReminder, DetailReminder, UpdateReminder, DeleteReminder)

urlpatterns = [
    path('', home, name='home'),
    path('card/', cards, name='cards'),

##########################################################################################

    path('create_status/', CreateStatus.as_view(), name='create_status'),
    path('status_list/', ListStatus.as_view(), name='status_list'),
    path('update_status/<int:pk>/', UpdateStatus.as_view(), name='update_status'),
    path('delete_status/<int:pk>/', DeleteStatus.as_view(), name='delete_status'),

##########################################################################################

    path('create_priority/', CreatePriority.as_view(), name='create_priority'),
    path('priority_list/', ListPriority.as_view(), name='priority_list'),
    path('update_piority/<int:pk>/', UpdatePriority.as_view(), name='update_priority'),
    path('delete_priority/<int:pk>/', DeletePriority.as_view(), name='delete_priority'),

##########################################################################################

    path('create_reminder/', CreateReminder.as_view(), name='create_reminder'),
    path('reminder_list/', ListReminder.as_view(), name='reminder_list'),
    path('reminder_detail/<int:pk>/', DetailReminder.as_view(), name='reminder_detail'),
    path('update_reminder/<int:pk>/', UpdateReminder.as_view(), name='update_reminder'),
    path('delete_reminder/<int:pk>/', DeleteReminder.as_view(), name='delete_reminder'),

]
