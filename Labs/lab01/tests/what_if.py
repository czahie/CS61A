test = {
  'name': 'What If?',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def xk(c, d):
          ...     if c == 4:
          ...         return 6
          ...     elif d >= 4:
          ...         return 6 + 7 + c
          ...     else:
          ...         return 25
          >>> xk(10, 10)
          23
          >>> xk(10, 6)
          23
          >>> xk(4, 6)
          6
          >>> xk(0, 0)
          25
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> def how_big(x):
          ...     if x > 10:
          ...         print('huge')
          ...     elif x > 5:
          ...         return 'big'
          ...     elif x > 0:
          ...         print('small')
          ...     else:
          ...         print("nothin'")
          >>> how_big(7)
          'big'
          >>> how_big(12)
          huge
          >>> how_big(1)
          small
          >>> how_big(-1)
          nothin'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> def so_big(x):
          ...     if x > 10:
          ...         print('huge')
          ...     if x > 5:
          ...         return 'big'
          ...     if x > 0:
          ...         print('small')
          ...     print("nothin'")
          >>> so_big(7)
          'big'
          >>> so_big(12)
          huge
          'big'
          >>> so_big(1)
          small
          nothin'
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> def ab(c, d):
          ...     if c > 5:
          ...         print(c)
          ...     elif c > 7:
          ...         print(d)
          ...     print('foo')
          >>> ab(10, 20)
          10
          foo
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> def bake(cake, make):
          ...    if cake == 0:
          ...        cake = cake + 1
          ...        print(cake)
          ...    if cake == 1:
          ...        print(make)
          ...    else:
          ...        return cake
          ...    return make
          >>> bake(0, 29)
          1
          29
          29
          >>> bake(1, "mashed potatoes")
          mashed potatoes
          'mashed potatoes'
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
