from math_series.series import fibonacci, lucas, sum_series

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

def test_lucas_1():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_2():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_lucas_3():
    actual = lucas(3)
    expected = 4
    assert actual == expected

def test_sum_series_0():
    actual = sum_series(0)
    expected = 0
    assert actual == expected 

def test_sum_series_negative_int():
    actual = sum_series(-1)
    expected = "nope"
    assert actual == expected 

def test_sum_series_2():
    actual = sum_series(2)
    expected = 0
    assert actual == expected 

def test_sum_series_optional_params():
    actual = sum_series(1,x=2,y=1)
    expected = 2
    assert actual == expected