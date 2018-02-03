test = {
  'name': 'Question 11',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> swap_strategy(13, 60, 8, 6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_strategy(30, 54, 8, 6)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_strategy(7, 23, 8, 6)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_strategy(7, 27, 8, 6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from tests.check_strategy import check_strategy
          >>> check_strategy(swap_strategy)
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
    },
    {
      'cases': [
        {
          'code': r"""
          >>> swap_strategy(10, 38, 8, 6) # beneficial
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_strategy(9, 1, 8, 6)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_strategy(35, 28, 8, 6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_strategy(37, 24, 8, 6)
          6
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
