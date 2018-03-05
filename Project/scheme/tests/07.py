test = {
  'name': 'Problem 7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'answer': '4159ecb5a05978a5a32e7f6101e4ff64',
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
          'locked': True,
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
          7adbbb2a725af942e401fe05085d85be
          # locked
          scm> 'hello
          7adbbb2a725af942e401fe05085d85be
          # locked
          scm> ''hello
          25378e4e94226b053c802e132f29644e
          # locked
          # choice: (quote hello)
          # choice: hello
          # choice: (hello)
          # choice: (quote (quote (hello)))
          scm> (quote (1 2))
          747eb81d19eb64f3a2f6281c19ddd315
          # locked
          scm> '(1 2)
          747eb81d19eb64f3a2f6281c19ddd315
          # locked
          scm> (quote (1 . 2))
          a7eb3cfaed53e2fcfd256a02363b59f7
          # locked
          scm> '(1 . (2))
          747eb81d19eb64f3a2f6281c19ddd315
          # locked
          scm> (car '(1 2 3))
          2894dd5fa65c8aa8f2b9d920d0e542e0
          # locked
          scm> (cdr '(1 2))
          368db613e63e51770ae2ae1c7859dd4b
          # locked
          scm> (car (car '((1))))
          2894dd5fa65c8aa8f2b9d920d0e542e0
          # locked
          scm> (quote 3)
          a3d16f1c59cdc683d6ce640b10aa5c1d
          # locked
          scm> (eval (cons 'car '('(4 2))))
          8ad686581488b3cc40d870a8db32810e
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
          >>> read_line(" (quote x) ")
          c45fd6efa08572418d68e7b8087d6602
          # locked
          # choice: Pair('x', nil)
          # choice: 'x'
          # choice: Pair('quote', 'x')
          # choice: Pair('quote', Pair('x', nil))
          >>> read_line(" 'x ")
          c45fd6efa08572418d68e7b8087d6602
          # locked
          # choice: Pair('x', nil)
          # choice: 'x'
          # choice: Pair('quote', 'x')
          # choice: Pair('quote', Pair('x', nil))
          >>> read_line(" (a b) ")
          6826a6bf9adff882c63a6e3b88e0785f
          # locked
          # choice: Pair('a', Pair('b', nil))
          # choice: Pair('quote', Pair(Pair('a', Pair('b', nil)), nil))
          # choice: Pair('quote', Pair('a', 'b'))
          # choice: Pair('quote', Pair('a', Pair('b', nil)))
          >>> read_line(" '(a b) ")
          05ab324acaaecfc3062ce99c0af5c9f4
          # locked
          # choice: Pair('a', Pair('b', nil))
          # choice: Pair('quote', Pair(Pair('a', Pair('b', nil)), nil))
          # choice: Pair('quote', Pair('a', 'b'))
          # choice: Pair('quote', Pair('a', Pair('b', nil)))
          >>> read_line(" '((a)) ")
          efd3a2d51557ef1a98c5fb19abc779fc
          # locked
          # choice: Pair('quote', Pair(Pair('a', nil), nil))
          # choice: Pair('quote', Pair(Pair('a', nil), nil), nil)
          # choice: Pair('quote', Pair(Pair('a'), nil))
          # choice: Pair('quote', Pair(Pair('a'), nil), nil)
          # choice: Pair('quote', Pair(Pair(Pair('a', nil), nil), nil))
          """,
          'hidden': False,
          'locked': True
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
