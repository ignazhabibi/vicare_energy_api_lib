from vicare_energy_api_lib.auth import hallo

def test_hallo():
    assert hallo("Welt") == "Hallo, Welt!"