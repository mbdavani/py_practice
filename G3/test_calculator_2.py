from Week_3.calculator import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) ==4
    assert square(-3) ==9

def test_zero():
    assert square(0) == 0

## "type pytest test_calculator_2.py" in the command line