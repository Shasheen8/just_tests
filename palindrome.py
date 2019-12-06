def Palindrome(mystr):
    try:
        mystr= "malayalam"
        rev_mystr= reversed(mystr)
        if (mystr == rev_mystr):
            return ("The string is a palindrome")
        else :
            return ("The string is not a palindrome")
    except ValueError:
        return "valid only for a string"


def test1():
    assert Palindrome("malayalam")

def test2():
    assert Palindrome("shasheen") =="The string is not a palindrome"

def test3():
    assert Palindrome("123")== "The string is not a palindrome"
