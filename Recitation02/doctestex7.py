"""
>>> type(this)
<class 'str'>
>>> type(that)
<class 'int'>
>>> type(something)
<class 'float'>
"""
# Place your solution code on the line after this one...
this = 'this is a string'
that = 3
something = 5.0

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
