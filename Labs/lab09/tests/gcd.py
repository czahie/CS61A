test = {
  'name': 'gcd',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (gcd 0 4)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (gcd 8 0)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (gcd 34 19)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (gcd 39 91)
          13
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (gcd 20 30)
          10
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (gcd 40 40)
          40
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
