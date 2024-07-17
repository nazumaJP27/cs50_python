from um import count


def test_count():
    assert count("Hi, um what a um... great! yum yum") == 2
    assert count("Hello, um, Umbrella Corps. Um... nice tyrant you guys have, um...") == 3
    assert count("Here in Umbrella Corps we trive on dehumanizations and latifundium curriculum") == 0
