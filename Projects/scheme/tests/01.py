test = {
  'name': 'Problem 1',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> scheme_read(Buffer(tokenize_lines(['nil'])))
          nil
          >>> scheme_read(Buffer(tokenize_lines(['1'])))
          1
          >>> scheme_read(Buffer(tokenize_lines(['true'])))
          True
          >>> read_line('3')
          3
          >>> read_line('-123')
          -123
          >>> read_line('1.25')
          1.25
          >>> read_line('true')
          True
          >>> read_line('(a)')
          Pair('a', nil)
          >>> read_line(')')
          SyntaxError
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> src = Buffer(tokenize_lines(["(+ 1 ", "(23 4)) ("]))
          >>> src.current()
          '('
          >>> src.remove_front()
          '('
          >>> src.current()
          '+'
          >>> src.remove_front()
          '+'
          >>> src.remove_front()
          1
          >>> scheme_read(src)  # If you're stuck, read the doctest for scheme_read in scheme_reader.py
          Pair(23, Pair(4, nil))
          >>> src.current()
          ')'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> scheme_read(Buffer(tokenize_lines(['(23 4)'])))
          Pair(23, Pair(4, nil))
          >>> read_line('(23 4)')  # Shorter version of above!
          Pair(23, Pair(4, nil))
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> read_tail(Buffer(tokenize_lines([')'])))
          nil
          >>> read_tail(Buffer(tokenize_lines(['1 2 3)'])))
          Pair(1, Pair(2, Pair(3, nil)))
          >>> read_tail(Buffer(tokenize_lines(['2 (3 4))'])))
          Pair(2, Pair(Pair(3, Pair(4, nil)), nil))
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> read_tail(Buffer(tokenize_lines(['(1 2 3)'])))
          SyntaxError
          >>> read_line('((1 2 3)')
          SyntaxError
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> src = Buffer(tokenize_lines(["(+ 1 2)"]))
          >>> scheme_read(src)
          Pair('+', Pair(1, Pair(2, nil)))
          >>> src.current() # Don't forget to remove the closing parenthesis!
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> read_line("(+ (- 2 3) 1)")
          Pair('+', Pair(Pair('-', Pair(2, Pair(3, nil))), Pair(1, nil)))
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> read_line("()")
          nil
          >>> read_line("((a))")
          Pair(Pair('a', nil), nil)
          >>> read_line("(+ 1 (- 2 3) 8)")
          Pair('+', Pair(1, Pair(Pair('-', Pair(2, Pair(3, nil))), Pair(8, nil))))
          # choice: Pair('+', Pair(1, Pair('-', Pair(2, 3), Pair(8, nil))))
          # choice: Pair('+', Pair(1, Pair(Pair('-', Pair(2, 3)), Pair(8, nil))))
          # choice: Pair('+', Pair(1, Pair('-', Pair(2, Pair(3, nil)), Pair(8, nil))))
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
