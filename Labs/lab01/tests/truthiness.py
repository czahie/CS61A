test = {
  'name': 'Truthiness',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 0 or True
          True
          >>> not '' or not 0 and False
          True
          >>> 13 and False
          False
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
          >>> False or 1
          1
          >>> '' or 1 and 1/0
          Error
          >>> not 0 and 12 or 0
          12
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
