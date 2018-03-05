test = {
  'name': 'Problem 16',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define y 1)
          17cb57908ef08e52f95d9f071151342f
          # locked
          scm> (define f (mu (x) (+ x y)))
          0f95edcd87e28fa8e0cb767981adc36d
          # locked
          scm> (define g (lambda (x y) (f (+ x x))))
          f52d1b972c48783316eb00d88d4d300f
          # locked
          scm> (g 3 7)
          82b58f6e2f61a1a4b7dee17cb8ac08e0
          # locked
          """,
          'hidden': False,
          'locked': True
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
          scm> (define h (mu () x))
          h
          scm> (define (high fn x) (fn))
          high
          scm> (high h 2)
          2
          scm> (define (f x) (mu () (lambda (y) (+ x y))))
          f
          scm> (define (g x) (((f (+ x 1))) (+ x 2)))
          g
          scm> (g 3)
          8
          scm> (mu ())
          SchemeError
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
