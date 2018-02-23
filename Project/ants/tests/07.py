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
          c9452203eb0b0f0bd2454586a6c2fc5c
          # locked
          >>> WallAnt.food_cost
          c9452203eb0b0f0bd2454586a6c2fc5c
          # locked
          """,
          'hidden': False,
          'locked': True
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
          d89cf7c79d5a479b0f636734143ed5e6
          # locked
          >>> bee.armor
          20e0ee99561cd5e38514075f77309e71
          # locked
          >>> wall.place is place
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          >>> bee.place is place
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          """,
          'hidden': False,
          'locked': True
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
