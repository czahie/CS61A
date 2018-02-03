test = {
  'name': 'Question 0',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> test_dice = make_test_dice(4, 1, 2)
          >>> test_dice()
          4
          >>> test_dice() # Second call
          1
          >>> test_dice() # Third call
          2
          >>> test_dice() # Fourth call
          4
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
