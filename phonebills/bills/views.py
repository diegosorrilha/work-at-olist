from django.http import JsonResponse


def phonebills(request):
    data = {
        'subscriber': request.GET['subscriber_phone'],
        'reference_period': request.GET['reference_period'],
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
