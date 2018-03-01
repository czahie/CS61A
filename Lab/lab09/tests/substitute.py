test = {
  'name': 'substitute',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (substitute '(c a b) 'b 'l)
          166376f57a3bec4eac131bfee76fa891
          # locked
          scm> (substitute '(f e a r s) 'f 'b)
          c62e166d1c0e8ea235c11a4819380d61
          # locked
          scm> (substitute '(g (o) o (o)) 'o 'r)
          f452b56e70a31fffc3f0e1e94ef68eae
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (substitute '((lead guitar) (bass guitar) (rhythm guitar) drums)
          ....               'guitar 'axe)
          ((lead axe) (bass axe) (rhythm axe) drums)
          scm> (substitute '(romeo romeo wherefore art thou romeo) 'romeo 'paris)
          (paris paris wherefore art thou paris)
          scm> (substitute '((to be) or not (to (be))) 'be 'eat)
          ((to eat) or not (to (eat)))
          scm> (substitute '(a b (c) d e) 'foo 'bar)
          (a b (c) d e)
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
