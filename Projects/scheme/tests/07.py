test = {
  'name': 'Problem 7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'answer': 'Pair(A, nil), where: A is the quoted expression',
          'choices': [
            r"""
            Pair('quote', Pair(A, nil)), where:
                A is the quoted expression
            """,
            r"""
            [A], where:
                A is the quoted expression
            """,
            r"""
            Pair(A, nil), where:
                A is the quoted expression
            """,
            r"""
            A, where:
                A is the quoted expression
            """
          ],
          'hidden': False,
          'locked': False,
          'question': 'What is the structure of the expressions argument to do_quote_form?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (quote hello)
          hello
          scm> 'hello
          hello
          scm> ''hello
          (quote hello)
          scm> (quote (1 2))
          (1 2)
          scm> '(1 2)
          (1 2)
          scm> (quote (1 . 2))
          (1 . 2)
          scm> '(1 . (2))
          (1 2)
          scm> (car '(1 2 3))
          1
          scm> (cdr '(1 2))
          (2)
          scm> (car (car '((1))))
          1
          scm> (quote 3)
          3
          scm> (eval (cons 'car '('(4 2))))
          4
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
          >>> read_line(" (quote x) ")
          Pair('quote', Pair('x', nil))
          >>> read_line(" 'x ")
          Pair('quote', Pair('x', nil))
          >>> read_line(" (a b) ")
          Pair('a', Pair('b', nil))
          >>> read_line(" '(a b) ")
          Pair('quote', Pair(Pair('a', Pair('b', nil)), nil))
          >>> read_line(" '((a)) ")
          Pair('quote', Pair(Pair(Pair('a', nil), nil), nil))
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> read_line("(a (b 'c))")
          Pair('a', Pair(Pair('b', Pair(Pair('quote', Pair('c', nil)), nil)), nil))
          >>> read_line("(a (b '(c d)))")
          Pair('a', Pair(Pair('b', Pair(Pair('quote', Pair(Pair('c', Pair('d', nil)), nil)), nil)), nil))
          >>> read_line("')")
          SyntaxError
          >>> read_line("'()")
          Pair('quote', Pair(nil, nil))
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> read_line("'('a)")
          Pair('quote', Pair(Pair(Pair('quote', Pair('a', nil)), nil), nil))
          >>> read_line("''a")
          Pair('quote', Pair(Pair('quote', Pair('a', nil)), nil))
          >>> read_line("'('('a 'b 'c))")
          Pair('quote', Pair(Pair(Pair('quote', Pair(Pair(Pair('quote', Pair('a', nil)), Pair(Pair('quote', Pair('b', nil)), Pair(Pair('quote', Pair('c', nil)), nil))), nil)), nil), nil))
          >>> read_line("(+ '(1 2) 3)")
          Pair('+', Pair(Pair('quote', Pair(Pair(1, Pair(2, nil)), nil)), Pair(3, nil)))
          >>> read_line("'('+ '(1 2) '3)")
          Pair('quote', Pair(Pair(Pair('quote', Pair('+', nil)), Pair(Pair('quote', Pair(Pair(1, Pair(2, nil)), nil)), Pair(Pair('quote', Pair(3, nil)), nil))), nil))
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> scheme_read(Buffer(tokenize_lines(["'hello"])))
          Pair('quote', Pair('hello', nil))
          >>> read_line("(car '(1 2))")
          Pair('car', Pair(Pair('quote', Pair(Pair(1, Pair(2, nil)), nil)), nil))
          >>> print(read_line("(car '(1 2))"))
          (car (quote (1 2)))
          >>> read_line("'('a)")
          Pair('quote', Pair(Pair(Pair('quote', Pair('a', nil)), nil), nil))
          >>> read_line("''a")
          Pair('quote', Pair(Pair('quote', Pair('a', nil)), nil))
          >>> read_line("'('('a 'b 'c))")
          Pair('quote', Pair(Pair(Pair('quote', Pair(Pair(Pair('quote', Pair('a', nil)), Pair(Pair('quote', Pair('b', nil)), Pair(Pair('quote', Pair('c', nil)), nil))), nil)), nil), nil))
          >>> read_line("(+ '(1 2) 3)")
          Pair('+', Pair(Pair('quote', Pair(Pair(1, Pair(2, nil)), nil)), Pair(3, nil)))
          >>> read_line("'('+ '(1 2) '3)")
          Pair('quote', Pair(Pair(Pair('quote', Pair('+', nil)), Pair(Pair('quote', Pair(Pair(1, Pair(2, nil)), nil)), Pair(Pair('quote', Pair(3, nil)), nil))), nil))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme_reader import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
