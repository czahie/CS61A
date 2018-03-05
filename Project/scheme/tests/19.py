test = {
  'name': 'Problem 19',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (let-to-lambda 1)
          2894dd5fa65c8aa8f2b9d920d0e542e0
          # locked
          scm> (let-to-lambda 'a)
          bcba5a8b5eb148269b808d42d0d4fef5
          # locked
          scm> (let-to-lambda '(+ 1 2))
          07bf87256cd8dfa90c86841a1d37643a
          # locked
          scm> (let-to-lambda '(let ((a 1)
          ....                 (b 2))
          ....                (+ a b)))
          a28e3e321fa8868c1949f68b122a8253
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> '(quoted expressions remain the same)
          (quoted expressions remain the same)
          scm> (let-to-lambda '(quote (let ((a 1) (b 2)) (+ a b))))
          (quote (let ((a 1) (b 2)) (+ a b)))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'questions)
      """,
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> '(lambda parameters not affected but body affected)
          (lambda parameters not affected but body affected)
          scm> (let-to-lambda '(lambda (let a b) (+ let a b)))
          (lambda (let a b) (+ let a b))
          scm> (let-to-lambda '(lambda (x) a (let ((a x)) a)))
          (lambda (x) a ((lambda (a) a) x))
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (let-to-lambda '(let ((a (let ((a 2)) a))
          ....                 (b 2))
          ....                (+ a b)))
          ((lambda (a b) (+ a b)) ((lambda (a) a) 2) 2)
          scm> (let-to-lambda '(let ((a 1))
          ....                (let ((b a))
          ....                     b)))
          ((lambda (a) ((lambda (b) b) a)) 1)
          scm> (let-to-lambda '(+ 1 (let ((a 1)) a)))
          (+ 1 ((lambda (a) a) 1))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'questions)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
