from src.models import Apartment
from src.manager import Manager
from src.models import Parameters
import pytest
import json


def test_load_data():
    parameters = Parameters()
    manager = Manager(parameters)
    assert isinstance(manager.apartments, dict)
    assert isinstance(manager.tenants, dict)
    assert isinstance(manager.transfers, list)
    assert isinstance(manager.bills, list)

    for apartment_key, apartment in manager.apartments.items():
        assert isinstance(apartment, Apartment)
        assert apartment.key == apartment_key
def test_manager_wczytuje_najemcow():
    parameters = Parameters()
    manager = Manager(parameters)
    with open(parameters.tenants_json_path, 'r') as file:
        tenants_data = json.load(file)
    
    expected_names = [
        tenant["name"] for tenant in tenants_data.values()
    ]
    for tenant_key, tenant in manager.tenants.items():
        assert tenant.name in expected_names, f"Najemca {tenant.name} nie znajduje się w pliku JSON!"