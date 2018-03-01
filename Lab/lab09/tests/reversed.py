test = {
  'name': 'Reversed',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from lab09_extra import *
          >>> reversed(Link(3, Link(4, Link(5))))
          Link(5, Link(4, Link(3)))
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
