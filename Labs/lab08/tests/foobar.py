test = {
  'name': 'FooBar',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> class Foo:
          ...     def print_one(self):
          ...         print('foo')
          ...     def print_two():
          ...         print('foofoo')
          >>> f = Foo()
          >>> f.print_one()
          foo
          >>> f.print_two()
          Error
          >>> Foo.print_two()
          foofoo
          >>> class Bar(Foo):
          ...     def print_one(self):
          ...         print('bar')
          >>> b = Bar()
          >>> b.print_one()
          bar
          >>> Bar.print_two()
          foofoo
          >>> Bar.print_one = lambda x: print('new bar')
          >>> b.print_one()
          new bar
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
