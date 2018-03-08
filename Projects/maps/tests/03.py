test = {
  'name': 'Problem 3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'answer': 'pair; e.g. [1, 1]',
          'choices': [
            'number; e.g. 1',
            "restaurant; e.g. make_restaurant('A', [1, 1], ['Food'], 1, [])",
            'pair; e.g. [1, 1]',
            "string of a pair; e.g. '[1, 1]'"
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          Which of the following types of values can be passed as
          an argument to distance?
          """
        },
        {
          'answer': 'lambda x: abs(x[0] - x[1])',
          'choices': [
            'lambda x, y: pow(-x, y)',
            'lambda x, y: abs(x - y)',
            'lambda x: abs(x[0] - x[1])',
            'sum'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          Consider the list l = [[4, 1], [-3, 2], [5, 0]]. Which of
          the choices below for fn would make min(l, key=fn) evaluate
          to [4, 1]?
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> distance([0, 0], [3, 4]) # should be a decimal
          5.0
          >>> distance([6, 1], [6, 1]) # should be a decimal
          0.0
          >>> distance([-2, 7], [-3.5, 9]) # should be a decimal
          2.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> find_closest([6, 1],
          ...              [[1, 5], [3, 3]])
          [3, 3]
          >>> find_closest([1, 6],
          ...              [[1, 5], [3, 3]])
          [1, 5]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> find_closest([0, 0],
          ...              [[-2, 0], [2, 0]])
          [-2, 0]
          >>> find_closest([0, 0],
          ...              [[1000, 1000]])
          [1000, 1000]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Be sure to use the distance function!
          >>> find_closest([0, 0],
          ...              [[2, 2], [0, 3]])
          [2, 2]
          >>> find_closest([0, 0],
          ...              [[5, 5], [2, 7]])
          [5, 5]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> find_closest([0, 0],
          ...              [[1, 0], [0, 1], [-1, 0], [0, -1]])
          [1, 0]
          >>> find_closest([0, 0],
          ...              [[0, 1], [1, 0], [0, -1], [-1, 0]])
          [0, 1]
          >>> find_closest([0, 0],
          ...              [[1, 1], [2, 2], [3, 3]])
          [1, 1]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import tests.test_functions as test
      >>> from recommend import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
