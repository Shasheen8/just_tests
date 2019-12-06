def Fact(num):
    try:
        if (num == 1):
            return num
        else:
            return num *Fact(num-1)
    except TypeError:
        return "positive numbers only"

        if (num<0):
            return False
        elif (num==0):
            return "Factorial of zero is 1"
        else:
            return ("Factorial of the ", num , "is", Fact(num))

    except ValueError:
        return "None"


def test1():
    assert Fact(2)== 2

def test2():
    assert Fact(4)==24

def test3():
    assert not Fact(5)== 100

def test4():
    assert Fact("abc")== "positive numbers only"
