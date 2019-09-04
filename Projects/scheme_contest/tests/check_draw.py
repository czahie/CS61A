test = {
  'name': 'Check Draw',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> with open('contest.scm') as f:
          ...     contents = f.read().strip()
          >>> last_line = contents.split('\n')[-1]
          >>> last_line == '(draw)'
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
