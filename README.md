Estoy aprendiendo a programar todavía asi que quice aprovechar la oportunidad de hacer este proyecto, que menciono el canal de Youtube "HolaMundo", en este video: "https://www.youtube.com/watch?v=Iy-jPHANSVg&t=441s".
Creo que cumple con lo que se pedía, la mayoría de las cosas las solucione yo, pero aún así para algunas cosas hice trampa y use chat gpt:

Con está función por ejemplo:

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

Como me gusto como me quedo tambien la desplegue en render, así que seguro tienen que hacer unos cambios si quieren usarla de manera local (debería bastar con comentar el database de postgre y descomentar el de la base sql).
Les dejo el enlace a render por si quieren chusmear.

https://recordatorios-n6kn.onrender.com
