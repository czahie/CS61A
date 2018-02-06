from lab03 import *

def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: y * 10 + x % 10
    while x > 0:
        x, y = x // 10, f()
    return y == n

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return n * skip_mul(n - 2)

def count_up(n):
    """Print out all numbers up to and including n in ascending order.

    >>> count_up(5)
    1
    2
    3
    4
    5
    """
    def counter(i):
        "*** YOUR CODE HERE ***"
        if i <= n:
            print(i)
            counter(i + 1)
    counter(1)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def calculate(i):
        if i < n:
            if n ** 0.5 % i == 0:  # 'n ** 0.5' could be replaced by 'n'
                return False
            else:
                return calculate(i + 1)
        else:
            return True
    return calculate(2)

def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    "*** YOUR CODE HERE ***"
# My solution
    def helper(i):
        total = 0
        if i + 1 <= n:
            return total + odd_term(i) + even_term(i + 1) + helper(i + 2)
        elif i <= n:
            return total + odd_term(i) + helper(i + 1)
        else:
            return total
    return helper(1)

# Official solution
    def helper(term0, term1, k):
        if k == n:
            return term0(k)
        return term0(k) + helper(term1, term0, k + 1)
    return helper(odd_term, even_term, 1)

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
# Could not figure it our until I saw the official solution
# "Do not use assignment statements" makes this question more difficult
    if n < 10:
        return 0
    else:
        return ten_pairs(n // 10) + count_digit(n // 10, 10 - n % 10)

def count_digit(n, digit):
    if n == 0:
        return 0
    elif n % 10 == digit:
        return count_digit(n // 10, digit) + 1
    else:
        return count_digit(n // 10, digit)



