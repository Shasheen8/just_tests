def Fizzbuzz(num):
    try:
        number = int(num)
        if (num % 3 == 0 and num % 5 == 0):
            return ("Fizzbuzz")
        if (num % 3 == 0):
            return ("Fizz")
        if (num % 5 == 0):
            return ("Buzz")
    except ValueError:
        return ("Enter Number")


def test1():
    assert Fizzbuzz(15) == "Fizzbuzz"

def test2():
    assert Fizzbuzz(9) == "Fizz"

def test3():
    assert Fizzbuzz(10) == "Buzz"

def test4():
    assert not Fizzbuzz(11) == "Buzz"

def test5():
    assert Fizzbuzz("abc") == "Enter Number"

def test6():
    assert Fizzbuzz(-30) == "Fizzbuzz"
