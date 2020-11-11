from math_series.series import fibonacci

def test_import():
    assert fibonacci

def test_fibonacci():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected 

def test_fibonacci_0():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected 

def test_fibonacci_2():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected 

def test_fibonacci_3():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected 

def test_fibonacci_4():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected 

def test_lucas_0():
    actual = lucas(0)
    expected = 2
    assert actual == expected
    