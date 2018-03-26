def scale(s, k):
    """Yield elements of the iterable s scaled by a number k.

    >>> s = scale([1, 5, 2], 5)
    >>> type(s)
    <class 'generator'>
    >>> list(s)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"
    for i in s:
        yield i * k

def countdown(n):
    """
    A generator that counts down from N to 0.
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    >>> for number in countdown(2):
    ...     print(number)
    ...
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"
# Solution 1
    while n >= 0:
        yield n
        n = n - 1

# Solution 2
    if n == 0:
        yield n
    else:
        yield n
        yield from countdown(n-1)

def trap(s, k):
    """Return a generator that yields the first K values in iterable S,
    but raises a ValueError exception if any more values are requested.

    >>> t = trap([3, 2, 1], 2)
    >>> next(t)
    3
    >>> next(t)
    2
    >>> next(t)
    ValueError
    >>> list(trap(range(5), 5))
    ValueError
    >>> t2 = trap(map(abs, reversed(range(-6, -4))), 2)
    >>> next(t2)
    5
    >>> next(t2)
    6
    >>> next(t2)
    ValueError
    """
    "*** YOUR CODE HERE ***"
    k_copy = k
    s_iter = iter(s)
    while k > 0:
        yield next(s_iter)
        k = k - 1
    else:
        raise ValueError("more than {} values are requested".format(k_copy))

# the naturals generator is used for testing scale and merge functions
def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1

