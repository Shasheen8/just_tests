def leap(number):
    n= int(number)
    if (n % 4) == 0:
        return True
    else:
        return False
    if (n % 100) == 0:
        return True
    else:
        return False
    if (n% 400) == 0 :
        return True
    else:
        return False



def test1():
    assert leap(2001)== False

def test2():
    assert leap(2014)== False

def test3():
    assert leap(2020)== True
