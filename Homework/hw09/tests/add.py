test = {
  'name': 'add',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (add odds 2)
          6af2f97663fe1ba5367bc92bc0a33fa9
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (add odds 5)
          85365f201091a10981b6fff0303aad4a
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (add odds 6)
          e37797e862fd4c43bb3092f44b7556e6
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (add odds 10)
          683abdd63e8c915d4ce0841477539c89
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
