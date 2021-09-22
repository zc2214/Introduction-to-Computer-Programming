"""
>>> s1 + s2 + s3
'Three strings were concatenated to make this string.'
"""
# Place your solution code on the line after this one...
s1 = 'Three strings '       #last space is important
s2 = 'were concatenated '   #last space is important
s3 = 'to make this string.'

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
