test = {
  'name': 'cyber-monday-part4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM total_bandwidth;
          85
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
