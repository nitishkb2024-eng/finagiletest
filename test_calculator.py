from calculator import add, subtract

def test_add():
    assert add(5, 3) == 8
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(1, 5) == -4
