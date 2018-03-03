test = {
  'name': 'nodots',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (nodots '(1 . 2))
          (1 2)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (nodots '(1 2 . 3))
          (1 2 3)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (nodots '((1 . 2) 3))
          ((1 2) 3)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (nodots '(1 (2 3 . 4) . 3))
          (1 (2 3 4) 3)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (nodots '(1 . ((2 3 . 4) . 3)))
          (1 (2 3 4) 3)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw09)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
