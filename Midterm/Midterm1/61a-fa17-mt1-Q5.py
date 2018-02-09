'''5. (10 points) Please Confirm
Definition. A confirming function for a sequence of digits, called a code, takes a single digit as its only
argument. If the digit does not match the first (left-most) digit of the code to be confirmed, it returns False.
If the digit does match, then the confirming function returns True if the code has only one digit, or another
confirming function for the rest of the code if there are more digits to confirm.
(a) (5 pt) Implement confirmer so that when confirmer takes a positive integer code, it returns a confirming
function for the digits of that code.'''

def confirmer(code):
    """Return a confirming function for CODE.
    >>> confirmer(204)(2)(0)(4) # The digits of 204 are 2, then 0, then 4.
    True
    >>> confirmer(204)(2)(0)(0) # The third digit of 204 is not 0.
    False
    >>> confirmer(204)(2)(1) # The second digit of 204 is not 1.
    False
    >>> confirmer(204)(20) # The first digit of 204 is not 20.
    False
    """
    def confirm1(d, t):
        def result(digit):
            if d == digit:
                return t
            else:
                return False
        return result

    def extend(prefix, rest):
        """Return a confirming function that returns REST when given the digits of PREFIX.
        For example, if c = extend(12, confirmer(34)), then c(1)(2) returns confirmer(34),
        so that c is a confirming function for 1234."""
        left, last = prefix // 10, prefix % 10
        if prefix < 10:
            return confirm1(prefix, rest)
        else:
            return extend(left, confirm1(last, rest)) # or extend(left, extend(last, rest))
    return extend(code, True)

'''(b) (5 pt) Given a confirming function, one can find the code it confirms, one digit at a time. Implement decode,
    which takes a confirming function f and returns the code that it confirms.
    from confirm_soln import confirmer'''

def decode(f, y=0):
    """Return the code for a confirming function f.
    >>> decode(confirmer(12001))
    12001
    >>> decode(confirmer(56789))
    56789
    """
    d = 0
    while d < 10:
        x, code = f(d), y * 10 + d
        if x == True:
            return code
        elif x == False:
            d = d+1
        else:
            return decode(x, code)