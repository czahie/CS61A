test = {
  'name': 'ordered?',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (ordered? '(1 2 3 4 5))  ; True or False
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (ordered? '(1 5 2 4 3))  ; True or False
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (ordered? '(2 2))  ; True or False
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (ordered? '(1 2 2 4 3))  ; True or False
          False
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
