import pytest

def isRecall(ycheck, syear, eyear):
    try:
        if (syear == 2015 and eyear == 2018):
            if (ycheck >= 2015 and ycheck <=2018):
                return True
            else:
                return False
    except ValueError:
        return ("Enter Integer")

def test1():
    assert isRecall(2016,2015,2018) == True

def test2():
    assert isRecall(2015,2015,2018) == True

def test3():
    assert isRecall(2012,2015,2018) == False

def test4():
    assert isRecall(0,2015,2018) == False

def test5():
    assert isRecall(-2015,2015,2018) == False



def test6():
    assert not isRecall(2015,1990,2000) == False

def test7():
    assert not isRecall(0,0,0) == False

def test8():
    assert not isRecall ("abcd",2015,2018) == "Enter Integer"
