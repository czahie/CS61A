test = {
  'name': 'Attributes',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> class Foo:
          ...     a = 10
          ...     def __init__(self, a):
          ...         self.a = a
          >>> class Bar(Foo):
          ...     b = 1
          >>> a = Foo(5)
          >>> b = Bar(2)
          >>> a.a
          5
          >>> b.a
          2
          >>> Foo.a
          10
          >>> Bar.b
          1
          >>> Bar.a
          10
          >>> b.b
          1
          >>> Foo.c = 15
          >>> Foo.c
          15
          >>> a.c
          15
          >>> b.c
          15
          >>> Bar.c
          15
          >>> b.b = 3
          >>> b.b
          3
          >>> Bar.b
          1
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
