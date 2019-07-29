from phonebills.bills.apps import BillsConfig


def test_if_app_bills_exists():
    assert BillsConfig.name == 'bills'
