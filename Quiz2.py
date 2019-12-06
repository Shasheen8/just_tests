#Preconditions
# income and threshold cannot be less than 0
# if income <threshold return 30%
# if income >= threshold  return 40%

def computeTaxRate(income, threshold):
    try:
        x= float(income)
        y= float(threshold)

        if (x<y):
            return 0.3
        if (x>=y ):
            return 0.4
        else:
            return False
    except ValueError as error:
        return "Only integers accepted"

def test1():
    assert computeTaxRate(999.99,1500) == 0.3

def test2():
    assert  computeTaxRate(1500,1500)== 0.4

def test3():

    print (computeTaxRate(1500.01,1500),"x")
    assert computeTaxRate(1500.01,1500)== 0.4

def test4():
    assert computeTaxRate(1600,1500)== 0.4

def test5():
    assert computeTaxRate(0,1500)== 0.3

def test6():
    assert computeTaxRate(-1000,1500)== 0.3

def test7():
    assert computeTaxRate("a",1500) == "Only integers accepted"

def test8():
    assert computeTaxRate(1500,2000) == 0.3

def test9():
    assert computeTaxRate(1500,-2000) ==0.4

def test10():
    assert computeTaxRate(1500,0) == 0.4

def test11():
    assert computeTaxRate(1500,"abc")== "Only integers accepted"

def test12():
    assert computeTaxRate(0,0)== 0.4

def test13():
    assert computeTaxRate(-1000,-1000)== 0.4
