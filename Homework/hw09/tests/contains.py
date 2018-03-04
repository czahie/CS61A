test = {
  'name': 'contains?',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (contains? odds 3)   ; True or False
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (contains? odds 9)   ; True or False
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (contains? odds 6)   ; True or False
          False
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
