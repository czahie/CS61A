test = {
  'name': 'Numpy check',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Ensure numpy is not imported
          >>> # You can only use standard libraries
          >>> 'numpy' not in modules
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'setup': r"""
      >>> import hog_contest
      >>> from sys import modules
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
