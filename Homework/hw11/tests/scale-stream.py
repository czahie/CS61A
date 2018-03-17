test = {
  'name': 'scale-stream',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (car s2)
          2
          scm> (car (cdr-stream s2))
          4
          scm> (car s4)
          4
          scm> (car (cdr-stream s4))
          8
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw11)
      scm> (define s (cons-stream 1 (cons-stream 2 nil)))
      scm> (define s2 (scale-stream s 2))
      scm> (define s4 (scale-stream s2 2))
      """,
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (car s2)
          2
          scm> (car (cdr-stream s2))
          2
          scm> (car (cdr-stream (cdr-stream s2)))
          2
          scm> (car (cdr-stream (cdr-stream s)))
          1
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw11)
      scm> (define s (cons-stream 1 s))
      scm> (define s2 (scale-stream s 2))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
