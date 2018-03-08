test = {
  'name': 'Question 10',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> bacon_strategy(0, 0, margin=8, num_rolls=5)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(70, 50, margin=8, num_rolls=5)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(50, 70, margin=8, num_rolls=5)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(32, 4, margin=5, num_rolls=4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(20, 18, margin=9, num_rolls=4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from tests.check_strategy import check_strategy
          >>> check_strategy(bacon_strategy)
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
          >>> bacon_strategy(20, 4, margin=3, num_rolls=4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(20, 23, margin=5, num_rolls=0)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(20, 24, margin=7, num_rolls=5)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(20, 25, margin=7, num_rolls=5)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(20, 26, margin=11, num_rolls=6)
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
