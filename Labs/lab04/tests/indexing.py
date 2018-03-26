test = {
  'name': 'List Indexing',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = [1, 3, [5, 7], 9] # Write the code that indexes into x to output the 7
          x[2][1]
          >>> x = [[7]] # Write the code that indexes into x to output the 7
          x[0][0]
          >>> x = [1, [2, [3, [4, [5, [6, [7]]]]]]] # Write the code that indexes into x to output the 7
          x[1][1][1][1][1][1][0]
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
          >>> lst = [3, 2, 7, [84, 83, 82]]
          >>> lst[4] # Write Error if this will error
          Error
          >>> lst = [3, 2, 7, [84, 83, 82]] # Write the code that indexes into lst to output the 82
          lst[3][2]
          >>> lst[3][0]
          84
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
