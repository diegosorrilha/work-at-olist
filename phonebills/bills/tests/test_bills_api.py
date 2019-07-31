from django.urls import reverse


def test_bill_status_code_200(client):
    response = client.get(reverse('phonebills'))
    assert response.status_code == 200
