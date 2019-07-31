import json

from django.urls import reverse

import pytest


@pytest.fixture
def expected_output():
    return {
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


def test_bill_status_code_200(client):
    data = {'subscriber_phone': '1199998899', 'reference_period': '12/2017'}
    response = client.get(reverse('phonebills'), data)
    assert response.status_code == 200


@pytest.mark.parametrize('phone', ['1199998899', '11988887766'])
def test_bill_get(expected_output, phone, client):
    month = '12'
    year = '2017'
    data = {'subscriber_phone': phone, 'reference_period': f'{month}/{year}'}
    response = client.get(reverse('phonebills'), data)
    parsed_data = json.loads(response.content)

    expected_output['subscriber'] = phone
    expected_output['reference_period'] = f'{month}/{year}'

    assert expected_output == parsed_data
