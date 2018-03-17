test = {
  'name': 'matchmaker',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM matchmaker LIMIT 10;
          panda|Havana|grey|blue
          panda|Havana|grey|blue
          wolf|Despacito|black|blue
          wolf|Despacito|black|purple
          wolf|Despacito|black|silver
          cat|Nyan Cat|orange|blue
          cat|Nyan Cat|orange|red
          cat|Nyan Cat|orange|cobalt
          cat|Nyan Cat|orange|orange
          cat|Nyan Cat|orange|blue
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
