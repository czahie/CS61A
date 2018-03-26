test = {
  'name': 'greatstudents',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM greatstudents;
          1/1|black|dragon|8|46
          1/1|blue|dog|60|69
          7/7|7|7|7|7
          7/7|7|7|7|7
          7/7|7|7|7|7
          12/31|blue|dog|50|50
          12/16|blue|dog|7|42
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab12.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
