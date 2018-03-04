test = {
  'name': 'add',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (add odds 2)
          (2 3 5 7 9)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (add odds 5)
          (3 5 7 9)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (add odds 6)
          (3 5 6 7 9)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (add odds 10)
          (3 5 7 9 10)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw09)
      scm> (define odds (list 3 5 7 9))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
