from django.http import JsonResponse
from .models import Reminder
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

import json

@csrf_exempt
def create_reminder(request):
    if request.method == 'POST':
        data = json.loads(request.body)  # Parse JSON data
        print(data)  # Debugging statement to print request data

        date = data.get('date')
        time = data.get('time')
        message = data.get('message')
        reminder_type = data.get('reminderType')

        if not date:
            return JsonResponse({'error': 'Date cannot be empty'}, status=400)

        reminder = Reminder.objects.create(
            date=date,
            time=time,
            message=message,
            reminder_type=reminder_type
        )

        return JsonResponse({'message': 'Reminder created successfully'}, status=201)

    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)