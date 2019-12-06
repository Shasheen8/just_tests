def fibo(n):
    try:
        if (n<=1):
            return n
        else:
            return (fibo(n-1) + fibo(n-2))


        nterms = 10
        if (nterms <=0):
            print("Enter only positive numbers")
        else:
            for i in range(nterms):
                return fibo(i)
    except TypeError:
        return "only numbers are valid"



def test1():
    assert fibo(5)

def test2():
    assert not fibo(0)

def test3():
    assert fibo(-2)

def test4():
    assert fibo("a") == "only numbers are valid"

def test5():
    assert fibo(20)

def test6():
    assert fibo(0+1) == 1

def test7():
    assert fibo((((0+1)+2)+3))== 8
