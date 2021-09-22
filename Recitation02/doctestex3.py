"""
>>> x + y
42
>>> type(message)
<class 'str'>
>>> len(message)
42
"""
# Place your solution code on the line after this one...
x = 42
y = 0
message = 42*'a'

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
