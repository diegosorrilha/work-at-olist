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
    response = client.get(reverse('phonebills'))
    assert response.status_code == 200


def test_bill_get(expected_output, client):
    response = client.get(reverse('phonebills'))
    parsed_data = json.loads(response.content)
    assert expected_output == parsed_data
