test = {
  'name': 'Restart',
  'points': 0,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': """
          >>> class IteratorA:
          ...    def __init__(self):
          ...        self.start = 10
          ...    def __next__(self):
          ...        if self.start > 100:
          ...            raise StopIteration
          ...        self.start += 20
          ...        return self.start
          ...    def __iter__(self):
          ...        return self
          >>> iterator = IteratorA()
          >>> [num for num in iterator]
          [30, 50, 70, 90, 110]
          >>> [num for num in iterator]
          []
          """,
        },
      ]
    },
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': """
          >>> class IteratorB:
          ...    def __init__(self):
          ...        self.start = -6
          ...    def __next__(self):
          ...        if self.start > 10:
          ...            raise StopIteration
          ...        self.start += 3
          ...        return self.start
          ...    def __iter__(self):
          ...        return self
          >>> iterator = IteratorB()
          >>> [num for num in iterator]
          [-3, 0, 3, 6, 9, 12]
          >>> [num for num in iterator]
          []
          """,
        },
      ]
    }
  ]
}