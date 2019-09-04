test = {
  'name': 'Problem 13',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (and)
          True
          scm> (and 1 False)
          False
          scm> (and (+ 1 1) 1)
          1
          scm> (and False 5)
          False
          scm> (and 4 5 (+ 3 3))
          6
          scm> (and True False 42 (/ 1 0))
          False
          """,
          'hidden': False,
          'locked': False
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
          False
          scm> (or (+ 1 1))
          2
          scm> (or False)
          False
          scm> (define (t) True)
          t
          scm> (or (t) 3)
          True
          scm> (or 5 2 1)
          5
          scm> (or False (- 1 1) 1)
          0
          scm> (or 4 True (/ 1 0))
          4
          """,
          'hidden': False,
          'locked': False
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
