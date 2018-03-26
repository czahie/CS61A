test = {
  'name': 'smallest-int-count',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM smallest_int_count LIMIT 50;
          0|1
          0.01|1
          1|163
          2|15
          3|13
          4|15
          5|4
          6|11
          7|13
          8|11
          9|6
          10|4
          11|14
          12|13
          13|8
          14|13
          15|4
          16|3
          17|21
          18|5
          19|9
          20|1
          21|2
          22|3
          23|24
          24|5
          25|3
          26|4
          27|8
          28|1
          29|3
          30|2
          31|8
          32|5
          33|3
          34|14
          36|2
          37|5
          38|1
          39|3
          40|1
          41|4
          42|2
          43|7
          46|2
          47|2
          48|2
          51|2
          53|2
          56|3
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
