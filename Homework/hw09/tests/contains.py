test = {
  'name': 'contains?',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (contains? odds 3)   ; True or False
          7346f33f3682a13d51291338e62f5a0f
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (contains? odds 9)   ; True or False
          7346f33f3682a13d51291338e62f5a0f
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (contains? odds 6)   ; True or False
          eb89d68eec1597c385d6e0ac3e3c6d52
          # locked
          """,
          'hidden': False,
          'locked': True
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
