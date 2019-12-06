def palindrome(text):
    s=text[::-1]
    if(s==text):
        return True
    return False

def test_1():
    assert palindrome("madam")

def test_2():
    assert not palindrome("Zack")

def test_3():
    assert  palindrome("123321")

def test_4():
    assert not palindrome("123abc")
 