test = {
  'name': 'Problem 1',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> HarvesterAnt.food_cost
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ThrowerAnt.food_cost
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing HarvesterAnt action
          >>> colony.food = 4
          >>> HarvesterAnt().action(colony)
          >>> colony.food
          5
          >>> HarvesterAnt().action(colony)
          >>> colony.food
          6
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      >>> hive, layout = Hive(make_test_assault_plan()), dry_layout
      >>> dimensions = (1, 9)
      >>> colony = AntColony(None, hive, ant_types(), layout, dimensions)
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
