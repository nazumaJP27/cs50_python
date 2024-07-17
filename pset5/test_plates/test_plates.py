from plates import is_valid


def test_is_valid():
    assert is_valid("AB1234") == True
    assert is_valid("abc123") == True
    assert is_valid("A12345") == False
    assert is_valid("AB1C23") == False
    assert is_valid("AB12345") == False
    assert is_valid("AB0123") == False
    assert is_valid("AB-123") == False
