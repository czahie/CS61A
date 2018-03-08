test = {
  'name': 'Question 2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> free_bacon(35)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(71)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(7)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(0)
          1
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
