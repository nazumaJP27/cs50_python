from twttr import shorten


def test_shorten():
    assert shorten("Laura") == "Lr"
    assert shorten("Manu") == "Mn"
    assert shorten("Alanis") == "lns"
    assert shorten("1234") == "1234"
    assert shorten("What's up?") == "Wht's p?"
