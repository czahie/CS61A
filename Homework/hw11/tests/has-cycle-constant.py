test = {
  'name': 'has-cycle-constant',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (has-cycle-constant s)
          False
          scm> (has-cycle-constant cycle)
          True
          scm> (has-cycle-constant cycle-within)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw11)
      scm> (define s (cons-stream 1 (cons-stream 1 nil)))
      scm> (define cycle (cons-stream 1 (cons-stream 2 cycle)))
      scm> (define cycle-within (cons-stream 1 (cons-stream 2 cycle)))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
