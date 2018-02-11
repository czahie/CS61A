HW_SOURCE_FILE = 'hw04.py'

###############
#  Questions  #
###############

def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st+ave)*(st+ave+1)//2 + ave

def street(inter):
    return w(inter) - avenue(inter)

def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2

w = lambda z: int(((8*z+1)**0.5-1)/2)

def taxicab(a, b):
    """Return the taxicab distance between two intersections.

    >>> times_square = intersection(46, 7)
    >>> ess_a_bagel = intersection(51, 3)
    >>> taxicab(times_square, ess_a_bagel)
    9
    >>> taxicab(ess_a_bagel, times_square)
    9
    """
    "*** YOUR CODE HERE ***"
    return abs(street(a) - street(b)) + abs(avenue(a) - avenue(b))

def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    "*** YOUR CODE HERE ***"

#  My solution
    from math import sqrt
    square_roots = []
    for integer in s:
        if int(sqrt(integer)) == sqrt(integer):
            square_roots = square_roots + [int(sqrt(integer))]
    return square_roots

# Official solution
    return [round(n ** 0.5) for n in s if round(n ** 0.5) ** 2 == n]

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    else:
        return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    "*** YOUR CODE HERE ***"
    i = 3
    num_1, num_2, num_3 = 1, 2, 3
    if n <= 3:
        return n
    else:
        while i < n:
            num_1, num_2, num_3 = num_2, num_3, num_3 + 2 * num_2 + 3 * num_1
            i += 1
    return num_3



def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
# My solution
    def contain(x):  # Equals to func have_seven
        """if number x contains digit 7, return True, else return False"""
        if x < 10:
            return x == 7
        else:
            return contain(x // 10) or contain(x % 10)

    def count(x=1, element=1, switch=0):
        """return the xth element of the ping-pong sequence
        element represents the xth element, switch records the times of the sequence changing direction"""
        if x == n:
            return element
        elif switch % 2 == 0:
            if contain(x) or x % 7 == 0:
                return count(x + 1, element - 1, switch + 1)
            else:
                return count(x + 1, element + 1, switch)
        elif switch % 2 == 1:
            if contain(x) or x % 7 == 0:
                return count(x + 1, element + 1, switch + 1)
            else:
                return count(x + 1, element - 1, switch)
    return count()

# Official solution
    def pingpong_next(k, p, up):
        if k == n:
            return p
        if up:
            return pingpong_switch(k + 1, p + 1, up)
        else:
            return pingpong_switch(k + 1, p - 1, up)

    def pingpong_switch(k, p, up):
        if k % 7 == 0 or has_seven(k):
            return pingpong_next(k, p, not up)
        else:
            return pingpong_next(k, p, up)

    return pingpong_next(1, 1, True)



def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
# My solution
    from math import pow

    def partitions(n, m):
        """Count the ways to partition n using parts up to m."""
        if n == 0:
            return 1
        elif n < 0:
            return 0
        elif m == 0:
            return 0
        else:
            return partitions(n - m, m) + partitions(n, m // 2)

    def find_largest_pow_2(x):
        """Find the largest power of two less than x"""
        i = 0
        while i < x:
            if pow(2, i) > x:
                return pow(2, i - 1)
            else:
                i += 1

    return partitions(amount, find_largest_pow_2(amount))

# Official solution (which is apparently better)
    return count_using(1, amount)

def count_using(min_coin, amount):
    if amount < 0:
        return 0
    elif amount == 0:
        return 1
    elif min_coin > amount:
        return 0
    else:
        with_min = count_using(min_coin, amount - min_coin)
        without_min = count_using(2*min_coin, amount)
        return with_min + without_min


###################
# Extra Questions #
###################

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return (lambda f: lambda k: f(f, k))(lambda f, k: k if k == 1 else mul(k, f(f, sub(k, 1))))  # Too hard
