from datetime import date

from django.http import JsonResponse, HttpResponseBadRequest


def phonebills(request):
    if 'subscriber_phone' not in request.GET:
        return HttpResponseBadRequest("It's required to pass the subscriber phone number!")
    if 'reference_period' in request.GET:
        reference_period = request.GET['reference_period']
    else:
        reference_period = f'{date.today().month-1}/{date.today().year}'

    data = {
        'subscriber': request.GET['subscriber_phone'],
        'reference_period': reference_period,
        'records': [
            {
                'destination': '1188887766',
                'start_date': '12',
                'start_time': '22:00:00',
                'duration': '7h59m59s',
                'price': 'R$ 0,36'
            }
        ]
    }

    return JsonResponse(data=data)
