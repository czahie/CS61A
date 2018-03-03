test = {
  'name': 'union',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (union odds (list 2 3 4 5))
          405d10ac20f44ebffdda6abe703d784e
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (union odds (list 2 4 6 8))
          ba4ca613f2e26b6b9d1f0d6fa699ce46
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (union odds eight)
          cc63269e5cede4114721942cc3cb9718
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
      scm> (define eight (list 1 2 3 4 5 6 7 8))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
