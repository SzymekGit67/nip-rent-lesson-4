import pytest

from pydantic import ValidationError
from src.models import Apartment
from src.models import Tenant


def test_apartment_fields():
    data = Apartment(
        key="apart-test",
        name="Test Apartment",
        location="Test Location",
        area_m2=50.0,
        rooms={
            "room-1": {"name": "Living Room", "area_m2": 30.0},
            "room-2": {"name": "Bedroom", "area_m2": 20.0}
        }
    )
    assert data.key == "apart-test"
    assert data.name == "Test Apartment"
    assert data.location == "Test Location"
    assert data.area_m2 == 50.0
    assert len(data.rooms) == 2, f"Oczekiwano 2 mieszkan ale znaleziono {len(data.rooms)}"


def test_apartment_from_dict():
    data = {
        "key": "apart-test",
        "name": "Test Apartment",
        "location": "Test Location",
        "area_m2": 50.0,
        "rooms": {
            "room-1": {"name": "Living Room", "area_m2": 30.0},
            "room-2": {"name": "Bedroom", "area_m2": 20.0}
        }
    }
    apartment = Apartment(**data)
    assert apartment.key == data["key"]
    assert apartment.name == data["name"]
    assert apartment.location == data["location"]
    assert apartment.area_m2 == data["area_m2"]
    assert len(apartment.rooms) == len(data["rooms"])

    data['area_m2'] = "25m2" # Invalid field
    with pytest.raises(ValidationError):
        wrong_apartment = Apartment(**data)



def test_czy_najemca_ma_wszystkie_pola_wypelnione():
    data = Tenant(
        name="imie_test",
        apartment="test_apart",
        room="test_room",
        rent_pln=6767.0,
        deposit_pln=7676.0,
        date_agreement_from="2024-01-01",
        date_agreement_to="2024-12-12",
    )
    assert data.name == "imie_test"
    assert data.apartment == "test_apart"
    assert data.room == "test_room"
    assert data.rent_pln == 6767.0
    assert data.deposit_pln == 7676.0
    assert data.date_agreement_from == "2024-01-01"
    assert data.date_agreement_to == "2024-12-12"

def test_najemca_dane():
    zledata = {
        "name": "Jan Kowalski",
        "apartment": "test_apart",
        "room": "test_room",
        "rent_pln": 1500.0,
        # Brak "deposit_pln"
        "date_agreement_from": "2024-01-01",
        "date_agreement_to": "2024-12-31"
    }
    tenant = Tenant(**zledata)
    assert tenant.name == "Jan Kowalski"
    assert tenant.apartment == "test_apart"
    assert tenant.room == "test_room"
    assert tenant.rent_pln == 1500.0
    assert tenant.deposit_pln == 2000.0
    assert tenant.date_agreement_from == "2024-01-01"
    assert tenant.date_agreement_to == "2024-12-31"
