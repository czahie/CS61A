test = {
  'name': 'meals-part1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM number_of_options;
          4
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read hw13.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
