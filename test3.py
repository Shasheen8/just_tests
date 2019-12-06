def Prime(number):
    for i in range(2,number+1):
        if (number % i == 0 and number>2):
            return (number, "The number is not a prime number")
        if (number<=0):
            return (number,"The number is not a prime number")
        else :
            return Prime

def test1():
    assert Prime(7)

def test2():
    assert not Prime(0)

def test():
    assert Prime(10)
