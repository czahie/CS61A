test = {
  'name': 'obedience',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM obedience LIMIT 10;
          You are not the boss of me!|Image 4|Image 3
          7|Image 3|Image 1
          7|Image 5|Image 4
          I do what I want.|Image 1|Image 5
          You are not the boss of me!|Image 2|Image 5
          Choose this option instead.|Image 2|Image 4
          I'm a rebel|Image 2|Image 1
          Choose this option instead.|Image 4|Image 5
          Choose this option instead.|Image 2|Image 1
          Choose this option instead.|Image 2|Image 3
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
