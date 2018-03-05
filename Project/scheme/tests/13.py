test = {
  'name': 'Problem 13',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (and)
          a87b4aa619df2eba30bc86785b816612
          # locked
          # choice: True
          # choice: False
          # choice: SchemeError
          scm> (and 1 False)
          55275a3300eb11ce47998c15403d99c6
          # locked
          # choice: 1
          # choice: True
          # choice: False
          scm> (and (+ 1 1) 1)
          2894dd5fa65c8aa8f2b9d920d0e542e0
          # locked
          scm> (and False 5)
          55275a3300eb11ce47998c15403d99c6
          # locked
          scm> (and 4 5 (+ 3 3))
          7964a777121da6350b0e6ecd16129317
          # locked
          scm> (and True False 42 (/ 1 0))
          55275a3300eb11ce47998c15403d99c6
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (and 3 2 False)
          False
          scm> (and 3 2 1)
          1
          scm> (and 3 False 5)
          False
          scm> (and 0 1 2 3)
          3
          scm> (define (true-fn) #t)
          true-fn
          scm> (and (true-fn))
          True
          scm> (define x False)
          x
          scm> (and x True)
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define x 0)
          x
          scm> (and (define x (+ x 1))
          ....      (define x (+ x 10))
          ....      (define x (+ x 100))
          ....      (define x (+ x 1000)))
          x
          scm> x
          1111
          scm> (define x 0)
          x
          scm> (and (define x (+ x 1))
          ....      (define x (+ x 10))
          ....      #f
          ....      (define x (+ x 100))
          ....      (define x (+ x 1000)))
          False
          scm> x
          11
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define (no-mutation) (and #t #t #t #t))
          no-mutation
          scm> no-mutation
          (lambda () (and True True True True))
          scm> (no-mutation)
          True
          scm> no-mutation ; `and` should not cause mutation
          (lambda () (and True True True True))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (or)
          55275a3300eb11ce47998c15403d99c6
          # locked
          scm> (or (+ 1 1))
          e56af2bab40778990634a527fe4407f8
          # locked
          scm> (or False)
          55275a3300eb11ce47998c15403d99c6
          # locked
          scm> (define (t) True)
          f16aec3dd21e3756aa445ca3e2d11a8d
          # locked
          scm> (or (t) 3)
          a87b4aa619df2eba30bc86785b816612
          # locked
          scm> (or 5 2 1)
          19a0c723c8c2fa9e2860916af61035e6
          # locked
          scm> (or False (- 1 1) 1)
          346bede49af9f8a0fafbc46acfa3395c
          # locked
          scm> (or 4 True (/ 1 0))
          8ad686581488b3cc40d870a8db32810e
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (or 0 1 2)
          0
          scm> (or 'a False)
          a
          scm> (or (< 2 3) (> 2 3) 2 'a)
          True
          scm> (or (< 2 3) 2)
          True
          scm> (define (false-fn) #f)
          false-fn
          scm> (or (false-fn) 'yay)
          yay
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define x 0)
          x
          scm> (or (begin (define x (+ x 1)) #f)
          ....     (begin (define x (+ x 10)) #f)
          ....     (begin (define x (+ x 100)) #f)
          ....     (begin (define x (+ x 1000)) #f))
          False
          scm> x
          1111
          scm> (define x 0)
          x
          scm> (or (begin (define x (+ x 1)) #f)
          ....     (begin (define x (+ x 10)) #f)
          ....     #t
          ....     (begin (define x (+ x 100)) #f)
          ....     (begin (define x (+ x 1000)) #f))
          True
          scm> x
          11
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define (no-mutation) (or #f #f #f #f))
          no-mutation
          scm> no-mutation
          (lambda () (or False False False False))
          scm> (no-mutation)
          False
          scm> no-mutation ; `or` should not cause mutation
          (lambda () (or False False False False))
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define (greater-than-5 x) (if (> x 5) #t #f))
          greater-than-5
          scm> (define (other y) (or (greater-than-5 y) #f))
          other
          scm> (other 2)
          False
          scm> (other 6) ; test for mutation
          True
          scm> (define (other y) (and (greater-than-5 y) #t))
          other
          scm> (other 2)
          False
          scm> (other 6) ; test for mutation
          True
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
