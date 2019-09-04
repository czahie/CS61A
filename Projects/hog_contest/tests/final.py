test = {
  'name': 'Time Check',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> for i in range(100):
          ...     for j in range(100):
          ...         assert -1 <= final_strategy(i, j) <= 10
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog_contest import final_strategy
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
