test = {
  'name': 'union',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (union odds (list 2 3 4 5))
          (2 3 4 5 7 9)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (union odds (list 2 4 6 8))
          (2 3 4 5 6 7 8 9)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (union odds eight)
          (1 2 3 4 5 6 7 8 9)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw09)
      scm> (define odds (list 3 5 7 9))
      scm> (define eight (list 1 2 3 4 5 6 7 8))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
