test = {
  'name': 'find',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (find m even?)
          2
          scm> (find m (lambda (x) (= x 3)))
          False
          scm> (find m (lambda (x) (= x 1)))
          1
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw11)
      scm> (define m (cons-stream 1 (cons-stream 2 nil)))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
