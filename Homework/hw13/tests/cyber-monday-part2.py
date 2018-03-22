test = {
  'name': 'cyber-monday-part2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM lowest_prices;
          Hallmart|GameStation|298.98
          Targive|QBox|390.98
          Targive|iBook|110.99
          RestBuy|kBook|94.99
          Hallmart|qPhone|85.99
          Hallmart|rPhone|69.99
          RestBuy|uPhone|89.99
          RestBuy|wBook|114.29
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
