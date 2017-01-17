#/usr/bin/python3
"""
This module supplies one function, add_integer(). For example,

>>> add_integer(4, 5)
9
"""

def add_integer(a, b):
    """
    Return the sum of 2 integers.
    >>> [add_integer(2, 3)]
    [5]
    >>> [add_integer(100.3, -2)]
    [98]
    >>> [add_integer(100.3, "School")]
    [b must be an integer]
    >>> [add_integer("Holberton", "School")]
    [a and b must be an integer]
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    if not (isinstance(a, int) and isinstance(b, int) or
            isinstance(a, float) and (b, float)):
        raise TypeError("a and b must be an integers or floats")
    return (a + b)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
