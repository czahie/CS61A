test = {
  'name': 'no-repeats',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (no-repeats (list 5 4 2))
          54dc7eb04dbc241999688c607936c8a6
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (no-repeats (list 5 4 5 4 2 2))
          54dc7eb04dbc241999688c607936c8a6
          # locked
          scm> (no-repeats (list 5 5 5 5 5))
          923ba3e7b2ee6f2ab24208f337bf0183
          # locked
          scm> (no-repeats ())
          f9ebafa0bfa75e2a858c464aa39a573d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (no-repeats '(5 4 3 2 1))
          (5 4 3 2 1)
          scm> (no-repeats '(5 4 3 2 1 1))
          (5 4 3 2 1)
          scm> (no-repeats '(5 5 4 3 2 1))
          (5 4 3 2 1)
          scm> (no-repeats '(12))
          (12)
          scm> (no-repeats '(1 1 1 1 1 1))
          (1)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'setup': r"""
      scm> (load 'lab09)
      scm> (load 'lab09_extra)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
