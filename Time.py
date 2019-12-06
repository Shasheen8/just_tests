def time(min, hours):
    m=int(min)
    h=int(hours)
    return (m*h)

def test1():
    assert time(60,2)

def test2():
    assert time(-60,-2)

    

