def greatest(num1,num2,num3):
    num_1=int(num1)
    num_2= int(num2)
    num_3 = int(num3)
    if ((num_1>num_2) and (num_1>num_3)):
        return (num_1, "is the largest")
    if ((num_2>num_1) and (num_2>num_3)):
        return (num_2, "is the largest")
    else :
        return (num_3, "is the largest")



def test1():
    assert greatest(2,3,5) == (5, "is the largest")

def test2():
    assert not greatest(3,1,5)== (3,"is not the largest")

def test3():
    assert greatest(9,1,1) == (9,"is the largest")

def test4():
    assert greatest(1,2,3)
