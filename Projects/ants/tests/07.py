test = {
  'name': 'Problem 7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing WallAnt parameters
          >>> wall = WallAnt()
          >>> wall.armor
          4
          >>> WallAnt.food_cost
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing WallAnt holds strong
          >>> place = colony.places['tunnel_0_4']
          >>> wall = WallAnt()
          >>> bee = Bee(1000)
          >>> place.add_insect(wall)
          >>> place.add_insect(bee)
          >>> for i in range(3):
          ...     bee.action(colony)
          ...     wall.action(colony)   # WallAnt does nothing
          >>> wall.armor
          1
          >>> bee.armor
          1000
          >>> wall.place is place
          True
          >>> bee.place is place
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      >>> hive, layout = Hive(AssaultPlan()), dry_layout
      >>> dimensions = (1, 9)
      >>> colony = AntColony(None, hive, ant_types(), layout, dimensions)
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
