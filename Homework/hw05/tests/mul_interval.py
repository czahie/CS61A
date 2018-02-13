test = {
  'name': 'mul_interval',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> str_interval(mul_interval(interval(-1, 2), interval(4, 8)))
          '-8 to 16'
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
          >>> str_interval(mul_interval(interval(-1, 2), interval(4, 8)))
          '-8 to 16'
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
