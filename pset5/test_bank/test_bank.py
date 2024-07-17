from bank import value


def test_value():
    assert value("Hello") == 0
    assert value("hi") == 20
    assert value("what's up?") == 100
    assert value("0123") == 100
    assert value("") == 100
