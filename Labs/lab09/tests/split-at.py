test = {
  'name': 'split-at',
  'points': 0,
  'suites': [
    {
      'type': 'scheme',
      'scored': True,
      'setup': """
      scm> (load 'lab09)
      scm> (load 'lab09_extra)
      """,
      'cases': [
        {
          'code': """
          scm> (car (split-at '(1 2 3 4 5) 3))
          (1 2 3)
          """,
          'hidden': False
        },
        {
          'code': """
          scm> (cdr (split-at '(1 2 3 4 5) 3))
          (4 5)
          """,
          'hidden': False
        },
        {
          'code': """
          scm> (car (split-at '(1 2 3 4 5) 10))
          (1 2 3 4 5)
          """,
          'hidden': False
        },
        {
          'code': """
          scm> (cdr (split-at '(1 2 3 4 5) 10))
          ()
          """,
          'hidden': False
        },
        {
          'code': """
          scm> (car (split-at '(0 1 1 2 3) 0))
          ()
          """,
          'hidden': False
        },
        {
          'code': """
          scm> (cdr (split-at '(0 1 1 2 3) 0))
          (0 1 1 2 3)
          """,
          'hidden': False
        },
      ]
    }
  ]
}
