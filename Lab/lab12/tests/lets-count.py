test = {
  'name': 'lets-count',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * from sp17favnum;
          7|25
          sqlite> SELECT * from sp17favpets;
          dragon|20
          dog|14
          cat|8
          unicorn|7
          n/a|6
          panda|5
          dolphin|4
          tiger|4
          7|3
          bear|3
          sqlite> SELECT * from fa17favpets;
          dog|57
          cat|33
          dragon|14
          panda|14
          tiger|14
          lion|13
          penguin|12
          dolphin|10
          john denero|9
          elephant|8
          sqlite> SELECT * from fa17dog;
          dog|57
          sqlite> SELECT * from fa17alldogs;
          dog|84
          sqlite> SELECT * from obedienceimages;
          7|Image 1|Image 1|7
          7|Image 1|Image 2|6
          7|Image 1|Image 3|16
          7|Image 1|Image 4|14
          7|Image 1|Image 5|11
          7|Image 2|Image 1|13
          7|Image 2|Image 2|10
          7|Image 2|Image 3|4
          7|Image 2|Image 4|1
          7|Image 2|Image 5|3
          7|Image 3|Image 1|13
          7|Image 3|Image 2|7
          7|Image 3|Image 3|6
          7|Image 3|Image 4|20
          7|Image 3|Image 5|10
          7|Image 4|Image 1|23
          7|Image 4|Image 2|13
          7|Image 4|Image 3|14
          7|Image 4|Image 4|18
          7|Image 4|Image 5|7
          7|Image 5|Image 1|12
          7|Image 5|Image 2|8
          7|Image 5|Image 3|7
          7|Image 5|Image 4|5
          7|Image 5|Image 5|5
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab12_extra.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
