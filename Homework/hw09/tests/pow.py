test = {
  'name': 'pow',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (pow 2 5)
          32
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (pow 10 3)
          1000
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (pow 3 3)
          27
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
