from django.http import JsonResponse


def phonebills(request):
    data = {
        'subscriber': '1199998877',
        'reference_period': '12/2017',
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
