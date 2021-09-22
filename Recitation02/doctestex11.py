"""
>>> a + b + c + d
50
>>> a - c
10
>>> a + b
20
"""
# Place your solution code on the line after this one...
a = 20
b = 0
c = 10
d = 20

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
