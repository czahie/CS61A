test = {
  'name': 'deep-map',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define (double x) (* 2 x))
          double
          scm> (deep-map double '(1 2 3 4))
          (2 4 6 8)
          scm> (deep-map double '(2 (3 4)))
          (4 (6 8))
          scm> (deep-map double '(1 2 3 (4) 5))
          (2 4 6 (8) 10)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'lab13)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
