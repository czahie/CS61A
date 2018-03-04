test = {
  'name': 'how-many-dots',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (how-many-dots '(1 2 3))
          0
          scm> (how-many-dots '(1 2 . 3))
          1
          scm> (how-many-dots '((1 . 2) 3 . 4))
          2
          scm> (how-many-dots '((((((1 . 2) . 3) . 4) . 5) . 6) . 7))
          6
          scm> (how-many-dots '(1 . (2 . (3 . (4 . (5 . (6 . (7))))))))
          0
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw10)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
