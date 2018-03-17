test = {
  'name': 'sevens',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM sevens;
          Choose this option instead.
          7
          7
          7
          7
          Choose this option instead.
          Choose this option instead.
          7
          7
          7
          7
          7
          7
          7
          7
          I'm a rebel
          I do what I want.
          YOLO!
          7
          7
          7
          YOLO!
          7
          7
          7
          7
          7
          7
          7
          7
          Choose this option instead.
          I do what I want.
          YOLO!
          Choose this option instead.
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
