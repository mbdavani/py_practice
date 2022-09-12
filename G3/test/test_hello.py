from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"
    assert hello("David") == "hello, David"


## Type the following line into the command box
#pytest test_hello.py