test = {
  'name': 'rle',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (rle '())
          ()
          scm> (stream-to-list (rle (list-to-stream '(1 2 3))))
          ((1 1) (2 1) (3 1))
          scm> (stream-to-list (rle (list-to-stream '(1 1 2 2 3 3))))
          ((1 2) (2 2) (3 2))
          scm> (define s (rle (list-to-stream '(1 1 1 1 1 6 6 6 6 2 5 5 5))))
          s
          scm> (stream-to-list s)          
          ((1 5) (6 4) (2 1) (5 3))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'lab13_extra)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
