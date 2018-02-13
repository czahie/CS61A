test = {
  'name': 'quadratic',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
          '-3 to 0.125'
          >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
          '0 to 10'
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hw05
      >>> from hw05 import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing for abstraction violations
          >>> # Your code should not check for which implementation is used
          >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
          '-3 to 0.125'
          >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
          '0 to 10'
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hw05
      >>> old_abstraction = hw05.interval, hw05.lower_bound, hw05.upper_bound
      >>> hw05.interval = lambda a, b: lambda x: a if x == 0 else b
      >>> hw05.lower_bound = lambda s: s(0)
      >>> hw05.upper_bound = lambda s: s(1)
      >>> from hw05 import *
      """,
      'teardown': r"""
      >>> hw05.interval, hw05.lower_bound, hw05.upper_bound = old_abstraction
      """,
      'type': 'doctest'
    }
  ]
}
