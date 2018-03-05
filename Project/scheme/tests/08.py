test = {
  'name': 'Problem 8',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> eval_all(Pair(2, nil), env)
          e56af2bab40778990634a527fe4407f8
          # locked
          # choice: 2
          # choice: (2)
          # choice: SchemeError
          >>> eval_all(Pair(4, Pair(5, nil)), env)
          19a0c723c8c2fa9e2860916af61035e6
          # locked
          # choice: 4
          # choice: (4)
          # choice: 5
          # choice: (5)
          # choice: SchemeError
          >>> eval_all(nil, env) # return None (meaning undefined)
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> lst = Pair(1, Pair(2, Pair(3, Pair(4, Pair(5, nil)))))
          >>> eval_all(lst, env)
          5
          >>> lst     # The list should not be mutated!
          Pair(1, Pair(2, Pair(3, Pair(4, Pair(5, nil)))))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme import *
      >>> env = create_global_frame()
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (begin (+ 2 3) (+ 5 6))
          bf10a0a8a47126dd73163da18664742b
          # locked
          scm> (begin (define x 3) x)
          a3d16f1c59cdc683d6ce640b10aa5c1d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (begin 30 '(+ 2 2))
          2b86d433000557e5796794c8fecad294
          # locked
          # choice: (+ 2 2)
          # choice: '(+ 2 2)
          # choice: 4
          # choice: 30
          scm> (define x 0)
          9d01e356a925e61e19645aef1b1fdd64
          # locked
          scm> (begin 42 (define x (+ x 1)))
          9d01e356a925e61e19645aef1b1fdd64
          # locked
          scm> x
          2894dd5fa65c8aa8f2b9d920d0e542e0
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (begin 30 'hello)
          hello
          scm> (begin (define x 3) (cons x '(y z)))
          (3 y z)
          scm> (begin (define x 3) (cons x '(x z)))
          (3 x z)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define x 0)
          x
          scm> (begin (define x (+ x 1))
          ....        (define x (+ x 10))
          ....        (define x (+ x 100))
          ....        (define x (+ x 1000)))
          x
          scm> x
          1111
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
