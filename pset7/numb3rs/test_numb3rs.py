from numb3rs import validate


def test_validate():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("0123.0.0.0") == False
    assert validate("275.500.0.0") == False
    assert validate("25.500.267.890") == False
    assert validate("dog") == False
