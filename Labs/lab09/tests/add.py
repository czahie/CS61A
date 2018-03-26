test = {
  'name': 'Add',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from lab09_extra import *
          >>> Link(1, Link(2)) + Link(3, Link(4, Link(5)))
          Link(1, Link(2, Link(3, Link(4, Link(5)))))
          >>> Link(1, Link(2)) + Link.empty
          Link(1, Link(2))
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