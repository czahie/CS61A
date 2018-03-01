test = {
  'name': 'gcd',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (gcd 0 4)
          eb5438773fa3774b23f3a524c49c4eb1
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (gcd 8 0)
          705c779aa26cefdacfc628f4e6fe0545
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (gcd 34 19)
          d912fc844d1dbaeea8a84b3ec8b315bc
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (gcd 39 91)
          5febbf9ecc14b7d17d82c63e8583d2a3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (gcd 20 30)
          1e136d20c59cd9c04d31c4f1f62f6c10
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (gcd 40 40)
          8545452e0022d856cdf4c9b7d8b57050
          # locked
          """,
          'hidden': False,
          'locked': True
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
