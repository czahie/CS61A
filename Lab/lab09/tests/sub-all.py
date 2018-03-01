test = {
  'name': 'sub-all',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (sub-all '(go ((bears))) '(go bears) '(big game))
          afe3b6edd6a72ec8a29b656de2661831
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (sub-all '((4 calling birds) (3 french hens) (2 turtle doves))
          ....     '(1 2 3 4)
          ....     '(one two three four))
          ((four calling birds) (three french hens) (two turtle doves))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'lab09)
      scm> (load 'lab09_extra)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
