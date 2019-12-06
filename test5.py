def pattern(s):
    try:
        for i in range(0,s):
            for j in range(0,i+1):
                return "*"
    except TypeError:
        return "put in values"


def test1():
    assert pattern("abd") == "put in values"

def test2():
    assert pattern("*") == "put in values"

def test3():
    assert pattern(9)

def test4():
    assert patt ern(100)

def test5():
    assert not pattern(9,3)
