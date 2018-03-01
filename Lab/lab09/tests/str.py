test = {
  'name': 'Add',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from lab09_extra import *
          >>> s = Link(1, Link(2, Link(3, Link(4))))
          >>> str(s)
          '<1, 2, 3, 4>'
          >>> print(Link(1))
          <1>
          >>> str(Link.empty)  # empty tuple
          '()'
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
