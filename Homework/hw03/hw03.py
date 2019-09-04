HW_SOURCE_FILE = 'hw03.py'

#############
# Questions #
#############

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
    "*** YOUR CODE HERE ***"
    if k < 10:
        return k == 7
    else:
        return has_seven(k // 10) or has_seven(k % 10)

def summation(n, term):

    """Return the sum of the first n terms in the sequence defined by term.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    "*** YOUR CODE HERE ***"
    if n == 1:
        return term(n)
    else:
        return term(n) + summation(n-1, term)

from operator import add, mul

def square(x):
    return x * x

def triple(x):
    return 3 * x

def identity(x):
    return x

def increment(x):
    return x + 1

def accumulate(combiner, base, n, term):
    """Return the result of combining the first n terms in a sequence and base.
    The terms to be combined are term(1), term(2), ..., term(n).  combiner is a
    two-argument commutative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)   # 2 * 1^2 * 2^2 * 3^2
    72
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return base
    else:
        return combiner(term(n), accumulate(combiner, base, n - 1, term))

def summation_using_accumulate(n, term):
    """Returns the sum of term(1) + ... + term(n). The implementation
    uses accumulate.

    >>> summation_using_accumulate(5, square)
    55
    >>> summation_using_accumulate(5, triple)
    45
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'summation_using_accumulate',
    ...       ['Recursion', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    return accumulate(add, 0, n, term)

def product_using_accumulate(n, term):
    """An implementation of product using accumulate.

    >>> product_using_accumulate(4, square)
    576
    >>> product_using_accumulate(6, triple)
    524880
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'product_using_accumulate',
    ...       ['Recursion', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    return accumulate(mul, 1, n, term)

def filtered_accumulate(combiner, base, pred, n, term):
    """Return the result of combining the terms in a sequence of N terms
    that satisfy the predicate PRED.  COMBINER is a two-argument function.
    If v1, v2, ..., vk are the values in TERM(1), TERM(2), ..., TERM(N)
    that satisfy PRED, then the result is
         BASE COMBINER v1 COMBINER v2 ... COMBINER vk
    (treating COMBINER as if it were a binary operator, like +). The
    implementation uses accumulate.

    >>> filtered_accumulate(add, 0, lambda x: True, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> filtered_accumulate(add, 11, lambda x: False, 5, identity) # 11
    11
    >>> filtered_accumulate(add, 0, odd, 5, identity)   # 0 + 1 + 3 + 5
    9
    >>> filtered_accumulate(mul, 1, greater_than_5, 5, square)  # 1 * 9 * 16 * 25
    3600
    >>> # Do not use while/for loops or recursion
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'filtered_accumulate',
    ...       ['While', 'For', 'Recursion'])
    True
    """
    def combine_if(x, y):
        "*** YOUR CODE HERE ***"
        if pred(x):  # The prerequisite of this statement is the fixed order (x, y) in combiner(x, y)
            return combiner(x, y)
        else:
            return y
    return accumulate(combine_if, base, n, term)

def odd(x):
    return x % 2 == 1

def greater_than_5(x):
    return x > 5

def make_repeater(f, n):
    """Return the function that computes the nth application of f.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> make_repeater(square, 0)(5)
    5
    """
    "*** YOUR CODE HERE ***"
    return accumulate(compose1, lambda x: x, n, lambda x: f)

# Alternatives

    def calculator(x):
        if n == 0:
            return x
        else:
            return f(make_repeater(f, n - 1)(x))
    return calculator





def compose1(f, g):
    """Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h

###################
# Extra Questions #
###################

quine = """
s='s="s="+repr(s)+";"+s;print(s)';s="s="+repr(s)+";"+s;print(s)
"""
quine1 =""" x = "print('x = %r;' % x, x)"; print('x = %r;' % x, x)"""

def zero(f):
    return lambda x: x

def successor(n):
    return lambda f: lambda x: f(n(f)(x))

def one(f):
    """Church numeral 1: same as successor(zero)"""
    "*** YOUR CODE HERE ***"
    return lambda x: f(x)

def two(f):
    """Church numeral 2: same as successor(successor(zero))"""
    "*** YOUR CODE HERE ***"
    return lambda x: f(f(x))

three = successor(two)

def church_to_int(n):
    """Convert the Church numeral n to a Python integer.

    >>> church_to_int(zero)
    0
    >>> church_to_int(one)
    1
    >>> church_to_int(two)
    2
    >>> church_to_int(three)
    3
    """
    "*** YOUR CODE HERE ***"
    f = lambda x: x + 1
    return n(f)(0)

def add_church(m, n):
    """Return the Church numeral for m + n, for Church numerals m and n.

    >>> church_to_int(add_church(two, three))
    5
    """
    "*** YOUR CODE HERE ***"
    return lambda f: lambda x: m(f)(n(f)(x))

def mul_church(m, n):
    """Return the Church numeral for m * n, for Church numerals m and n.

    >>> four = successor(three)
    >>> church_to_int(mul_church(two, three))
    6
    >>> church_to_int(mul_church(three, four))
    12
    """
    "*** YOUR CODE HERE ***"
    return lambda x: m(n(x))

def pow_church(m, n):
    """Return the Church numeral m ** n, for Church numerals m and n.

    >>> church_to_int(pow_church(two, three))
    8
    >>> church_to_int(pow_church(three, two))
    9
    """
    "*** YOUR CODE HERE ***"
    return lambda x: n(m)(x)
