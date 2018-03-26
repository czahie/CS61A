test = {
  'name': 'Odds and Evens',
  'points': 0,
  'suites': [
    {
      'type': 'wwpp',
      'scored': False,
      'cases': [
        {
          'code': """
          >>> class OddNaturalsIterator():
          ...     def __init__(self):
          ...         self.current = 1
          ...     def __next__(self):
          ...         result = self.current
          ...         self.current += 2
          ...         return result
          ...     def __iter__(self):
          ...         return self
          >>> odds = OddNaturalsIterator()
          >>> odd_iter1 = iter(odds)
          >>> odd_iter2 = iter(odds)
          >>> next(odd_iter1)
          1
          >>> next(odd_iter1)
          3
          >>> next(odd_iter1)
          5
          >>> next(odd_iter2)
          7
          >>> next(odd_iter1)
          9
          >>> next(odd_iter2)
          11
          """,
        },
        {
          'code': """
          >>> class EvenNaturalsIterator():
          ...     def __init__(self):
          ...         self.current = 0
          ...     def __next__(self):
          ...         result = self.current
          ...         self.current += 2
          ...         return result
          ...     def __iter__(self):
          ...         return EvenNaturalsIterator()
          >>> evens = EvenNaturalsIterator()
          >>> even_iter1 = iter(evens)
          >>> even_iter2 = iter(evens)
          >>> next(even_iter1)
          0
          >>> next(even_iter1)
          2
          >>> next(even_iter1)
          4
          >>> next(even_iter2)
          0
          >>> next(even_iter2)
          2
          """,
        },
      ]
    },
    {
      'type': 'wwpp',
      'scored': False,
      'cases': [
        {
          'code': """
          >>> class DoubleIterator():
          ...     def __init__(self):
          ...         self.current = 2
          ...     def __next__(self):
          ...         result = self.current
          ...         self.current += result
          ...         return result
          ...     def __iter__(self):
          ...         return DoubleIterator()
          >>> doubleI = DoubleIterator()
          >>> dIter = iter(doubleI)
          >>> next(doubleI)
          2
          >>> next(doubleI)
          4
          >>> next(dIter)
          2
          >>> next(dIter)
          4
          >>> next(doubleI)
          8
          """,
        },
        {
          'code': """
          >>> class ThreeIterator():
          ...     def __init__(self):
          ...         self.current = 10
          ...     def __next__(self):
          ...         result = self.current
          ...         self.current -= 3
          ...         return result
          ...     def __iter__(self):
          ...         return self
          >>> threeI = ThreeIterator()
          >>> tIter = iter(threeI)
          >>> next(threeI)
          10
          >>> next(threeI)
          7
          >>> next(tIter)
          4
          >>> next(tIter)
          1
          >>> next(threeI)
          -2
          """,
        }
      ]
    }
  ]
}