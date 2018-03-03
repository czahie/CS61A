test = {
  'name': 'intersect',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (intersect odds (list 2 3 4 5))
          ce54fefa36f4b271edf41f71e3b7c9d5
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (intersect odds (list 2 4 6 8))  ; Empty list is ()
          010af2cd1e765be62ece0c49314e61bd
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (intersect odds eight)
          ecd385deb9fde22b9af8f06330e4cbfc
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
