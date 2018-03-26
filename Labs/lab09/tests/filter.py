test = {
  'name': 'filter',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (filter even? '(1 2 3 4))
          (2 4)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (filter odd? '(1 3 5))
          (1 3 5)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (filter odd? '(2 4 6 1))
          (1)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (filter even? '(3))
          ()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (filter odd? nil)
          ()
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'lab09)
      scm> (load 'lab09_extra)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
