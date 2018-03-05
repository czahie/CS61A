test = {
  'name': 'Problem 15',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define x 1)
          9d01e356a925e61e19645aef1b1fdd64
          # locked
          scm> (let ((x 5))
          ....    (+ x 3))
          7160af5f6893bd49bb63dee6b8320930
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
          scm> (let ((a 1) (b a)) b)
          87c30138f7979b4f5a454aacfb191b98
          # locked
          # choice: SchemeError
          # choice: 1
          # choice: x
          # choice: y
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (let ((x 5))
          ....    (let ((x 2)
          ....          (y x))
          ....        (+ y (* x 2))))
          5fb541ba24eaf504edc7eae61bda4f97
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (define (square x) (* x x))
          square
          scm> (define (f x y)
          ....    (let ((a (+ 1 (* x y)))
          ....          (b (- 1 y)))
          ....        (+ (* x (square a))
          ....           (* y b)
          ....           (* a b))))
          f
          scm> (f 3 4)
          456
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
          scm> (define x 3)
          x
          scm> (define y 4)
          y
          scm> (let ((x (+ y 2))
          ....       (y (+ x 2)))
          ....      (cons x y))
          (6 . 5)
          scm> (let ((x 'hello)) x)
          hello
          scm> (let ((a 1) (b 2) (c 3)) (+ a b c))
          6
          scm> (define z 0)
          z
          scm> (let ((a (define z (+ z 1)))) z)
          1
          scm> (let ((x 1)
          ....       (y 3))
          ....    (define x (+ x 1))
          ....    (cons x y))
          (2 . 3)
          scm> (let ((a 1 1)) a)
          SchemeError
          scm> (let ((a 1) (2 2)) a)
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
