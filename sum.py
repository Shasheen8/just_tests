def sum(number):
    try:
        n= int(number)
        if (n<=1):
            return (n)
        else :
            return (n) + sum(n-1)
    except ValueError:
        return "numbers only"


def test1():
    assert sum(5)==15

def test2():
    assert sum(16)==136

def test3():
    assert not sum (10)== 100

def test4():
    assert sum("a")== "numbers only"
