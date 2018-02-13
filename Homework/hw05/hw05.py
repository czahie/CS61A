# Tree definition

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])

def replace_leaf(t, old, new):
    """Returns a new tree where every leaf value equal to old has
    been replaced with new.

    >>> yggdrasil = tree('odin',
    ...                  [tree('balder',
    ...                        [tree('thor'),
    ...                         tree('loki')]),
    ...                   tree('frigg',
    ...                        [tree('thor')]),
    ...                   tree('thor',
    ...                        [tree('sif'),
    ...                         tree('thor')]),
    ...                   tree('thor')])
    >>> laerad = copy_tree(yggdrasil) # copy yggdrasil for testing purposes
    >>> print_tree(replace_leaf(yggdrasil, 'thor', 'freya'))
    odin
      balder
        freya
        loki
      frigg
        freya
      thor
        sif
        freya
      freya
    >>> laerad == yggdrasil # Make sure original tree is unmodified
    True
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        if label(t) == old:
            return tree(new)
        return t
    else:
        return tree(label(t), [replace_leaf(b, old, new) for b in branches(t)])

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
#  Too hard, cannot figure it our on my own
    if n == 1:
        print_move(start, end)
    else:
        # The order is like this:
        # move all the other disks to the other rod, then move the largest one to end,
        # finally move the all the other disks to the end upon the largest one.
        other = 6 - start - end
        move_stack(n - 1, start, other)  # n - 1 represents all the other disks except the largest one at bottom
        print_move(start, end)
        move_stack(n - 1, other, end)



def interval(a, b):
    """Construct an interval from a to b."""
    return [a, b]

def lower_bound(x):
    """Return the lower bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[0]

def upper_bound(x):
    """Return the upper bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[1]

def str_interval(x):
    """Return a string representation of interval x."""
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y."""
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y."""
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y."""
    "*** YOUR CODE HERE ***"
    lower = lower_bound(x) - upper_bound(y)
    upper = upper_bound(x) - lower_bound(y)
    return interval(lower, upper)

# Official solution
    negative_y = interval(-upper_bound(y), -lower_bound(y))
    return add_interval(x, negative_y)

def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided by
    any value in y. Division is implemented as the multiplication of x by the
    reciprocal of y."""
    "*** YOUR CODE HERE ***"
    assert not lower_bound(y) <= 0 <= upper_bound(y), "interval that spans zero cannot be used as a divisor"
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))

def check_par():
    """Return two intervals that give different results for parallel resistors.

    >>> r1, r2 = check_par()
    >>> x = par1(r1, r2)
    >>> y = par2(r1, r2)
    >>> lower_bound(x) != lower_bound(y) or upper_bound(x) != upper_bound(y)
    True
    """
    r1 = interval(1, 2) # Replace this line!
    r2 = interval(3, 4) # Replace this line!
    return r1, r2

def multiple_references_explanation():
    return """The multiple reference problem...
    Eva is right. Because when an uncertain number is used in computation, the interval span will extend no matter which
    arithmetic is used(sub, add, mul, div). The less these number is used, the tighter the error bounds would be.
    
    
    The multiple reference problem exists.  The true value
    within a particular interval is fixed (though unknown).  Nested
    combinations that refer to the same interval twice may assume two different
    true values for the same interval, which is an error that results in
    intervals that are larger than they should be.

    Consider the case of i * i, where i is an interval from -1 to 1.  No value
    within this interval, when squared, will give a negative result.  However,
    our mul_interval function will allow us to choose 1 from the first
    reference to i and -1 from the second, giving an erroneous lower bound of
    -1.

    Hence, a program like par2 is better than par1 because it never combines
    the same interval more than once."""

def quadratic(x, a, b, c):
    """Return the interval that is the range of the quadratic defined by
    coefficients a, b, and c, for domain interval x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    "*** YOUR CODE HERE ***"

# My solution

    t = - b / (2 * a)  # f'(t) = 0
    t_case = a * t * t + b * t + c
    edge_case1 = a * lower_bound(x) * lower_bound(x) + b * lower_bound(x) + c
    edge_case2 = a * upper_bound(x) * upper_bound(x) + b * upper_bound(x) + c
    if lower_bound(x) <= t <= upper_bound(x):
        lower = min(t_case, edge_case1, edge_case2)
        upper = max(t_case, edge_case1, edge_case2)
    else:
        lower = min(edge_case1, edge_case2)
        upper = max(edge_case1, edge_case2)
    return interval(lower, upper)

# Official solution
    extremum = -b / (2*a)
    f = lambda x: a * x * x + b * x + c
    l, u, e = map(f, (lower_bound(x), upper_bound(x), extremum))
    if extremum >= lower_bound(x) and extremum <= upper_bound(x):
        return interval(min(l, u, e), max(l, u, e))
    else:
        return interval(min(l, u), max(l, u))



# My solution
# Failed the 3rd doctest because there are more than 1 zero point in df but I only find one from guess=1

def polynomial(x, c):
    """Return the interval that is the range of the polynomial defined by
    coefficients c, for domain interval x.

    >>> str_interval(polynomial(interval(0, 2), [-1, 3, -2]))
    '-3 to 0.125'
    >>> str_interval(polynomial(interval(1, 3), [1, -3, 2]))
    '0 to 10'
    >>> str_interval(polynomial(interval(0.5, 2.25), [10, 24, -6, -8, 3]))
    '18.0 to 23.0'
    """
    "*** YOUR CODE HERE ***"
    def polynomial_root():
        def df(x, k=len(c)):  # The df of the polynomial
            if k == 1:
                return 0
            else:
                return (k - 1) * c[k - 1] * pow(x, k - 2) + df(x, k - 1)

        def ddf(x, k=len(c)):  # The ddf of the polynomial
            if k == 1:
                return 0
            elif k == 2:
                return 0
            else:
                return (k - 2) * (k - 1) * c[k - 1] * pow(x, k - 3) + ddf(x, k - 1)
        return find_zero(df, ddf)

    t = polynomial_root()
    t_case, edge_case1, edge_case2 = 0, 0, 0
    k = len(c)
    while k > 0:
        edge_case1 += c[k - 1] * pow(lower_bound(x), k - 1)
        edge_case2 += c[k - 1] * pow(upper_bound(x), k - 1)
        t_case += c[k - 1] * pow(t, k - 1)
        k -= 1
    if lower_bound(x) <= t <= upper_bound(x):
        lower = min(t_case, edge_case1, edge_case2)
        upper = max(t_case, edge_case1, edge_case2)
    else:
        lower = min(edge_case1, edge_case2)
        upper = max(edge_case1, edge_case2)
    return interval(lower, upper)

# Newton's Method from lecture


from math import pow

def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance


def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess


def newton_update(f, df):
    def update(x):
        return x - f(x)/df(x)
    return update


def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)


# Official solution

def polynomial(x, c):
    """Return the interval that is the range of the polynomial defined by
    coefficients c, for domain interval x.

    >>> str_interval(polynomial(interval(0, 2), [-1, 3, -2]))
    '-3 to 0.125'
    >>> str_interval(polynomial(interval(1, 3), [1, -3, 2]))
    '0 to 10'
    >>> str_interval(polynomial(interval(0.5, 2.25), [10, 24, -6, -8, 3]))
    '18.0 to 23.0'
    """
    def add_fn(coeff, k, f):
        return lambda x: coeff * pow(x, k) + f(x)

    def add_dfn(coeff, k, df):
        return lambda x: k * coeff * pow(x, k-1) + df(x)

    def add_ddfn(coeff, k, ddf):
        return lambda x: k * (k-1) * coeff * pow(x, k-2) + ddf(x)

    # Define the polynomial and its first and second derivatives.
    f = lambda x: 0
    df = lambda x: 0
    ddf = lambda x: 0
    for k, coeff in enumerate(c):
        # Actually it's a recursive call. It's a little bit different cause it's from bottom to top
        # as this statement processes, f updates ( and a new lambda func is defined every time this statement executed)
        f = add_fn(coeff, k, f)
        if k > 0:
            df = add_dfn(coeff, k, df)
        if k > 1:
            ddf = add_ddfn(coeff, k, ddf)

    # Find as many extreme points as we can using Newton's method
    lower, upper = lower_bound(x), upper_bound(x)
    num_steps = 20
    step = (upper - lower) / num_steps
    starts = [lower + k * step for k in range(num_steps)]
    extremums = [find_zero(df, ddf, n) for n in starts]

    # Filter for the interval x and return
    ns = [n for n in extremums if n > lower and n < upper] + [lower, upper]
    values = [f(n) for n in ns]
    return interval(min(values), max(values))

# Newton's method from lecture

def improve(update, close, guess=1, max_updates=100):
    """Iteratively improve guess with update until close(guess) is true or
    max_updates have been applied."""
    k = 0
    while not close(guess) and k < max_updates:
        guess = update(guess)
        k = k + 1
    return guess

def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance

def find_zero(f, df, guess=1):
    """Return a zero of the function f with derivative df."""
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero, guess)

def newton_update(f, df):
    """Return an update function for f with derivative df,
    using Newton's method."""
    def update(x):
        return x - f(x) / df(x)
    return update


