"""
>>> type(thing1)
<class 'float'>
>>> type(thing2)
<class 'int'>
>>> type(thing3)
<class 'str'>
"""
# Place your solution code on the line after this one...
thing1 = 2.5
thing2 = 6
thing3 = 'Hello World!'

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
