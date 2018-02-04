test = {
  'name': 'Lambda the Free',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> lambda x: x # Remember to write Function if it's a function, Error if it errors, and Nothing if nothing is displayed.
          Function
          >>> a = lambda x: x
          >>> a(5)  # x is the parameter for the lambda function
          5
          >>> b = lambda: 3
          >>> b()
          3
          >>> c = lambda x: lambda: print('123')
          >>> c(88)
          Function
          >>> c(88)()
          123
          >>> d = lambda f: f(4)  # They can have functions as arguments as well.
          >>> def square(x):
          ...     return x * x
          >>> d(square)
          16
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> t = lambda f: lambda x: f(f(f(x)))
          >>> s = lambda x: x + 1
          >>> t(s)(0)
          3
          >>> bar = lambda y: lambda x: pow(x, y)
          >>> bar()(15)
          Error
          >>> foo = lambda: 32
          >>> foobar = lambda x, y: x // y
          >>> a = lambda x: foobar(foo(), bar(4)(x))
          >>> a(2)
          2
          >>> b = lambda x, y: print('summer')
          Nothing
          >>> c = b(4, 'dog')
          summer
          >>> print(c)
          None
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> a = lambda b: b * 2
          Nothing
          >>> a
          Function
          >>> a(a(a(2)))
          16
          >>> a(a(a()))
          Error
          >>> def d():
          ...     print(None)
          ...     print('whoo')
          >>> b = d()
          None
          whoo
          >>> b
          Nothing
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> x, y, z = 1, 2, 3
          >>> a = lambda b: x + y + z
          >>> x += y
          >>> y -= z
          >>> a('b')
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> z = 3
          >>> e = lambda x: lambda y: lambda: x + y + z
          >>> e(0)(1)()
          4
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
