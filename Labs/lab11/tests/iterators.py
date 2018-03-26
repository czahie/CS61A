test = {
  'name': 'Iterators',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> s = [1, [2, [3, [4]]]]
          >>> t = iter(s)
          >>> next(t)
          1
          >>> next(iter(next(t)))
          2
          >>> list(t)
          []
          >>> next(map(lambda x: x * x, filter(lambda y: y > 4, range(10))))
          25
          >>> r = iter(reversed(range(10000)))
          >>> next(r) - next(r)
          1
          >>> xs = [2, 3, 4, 5]
          >>> y, z = iter(xs), iter(xs)
          >>> next(zip(y, z))
          (2, 2)
          >>> next(zip(y, y))
          (3, 4)
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
