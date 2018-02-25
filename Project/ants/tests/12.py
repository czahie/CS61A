test = {
  'name': 'Problem 12',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing TankAnt parameters
          >>> TankAnt.food_cost
          6
          >>> TankAnt.damage
          1
          >>> TankAnt.container
          True
          >>> tank = TankAnt()
          >>> tank.armor
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing TankAnt action
          >>> tank = TankAnt()
          >>> place = colony.places['tunnel_0_1']
          >>> place.add_insect(tank)
          >>> for _ in range(3):
          ...     place.add_insect(Bee(3))
          >>> tank.action(colony)
          >>> [bee.armor for bee in place.bees]
          [2, 2, 2]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing TankAnt container methods
          >>> tank = TankAnt()
          >>> thrower = ThrowerAnt()
          >>> place = colony.places['tunnel_0_1']
          >>> place.add_insect(thrower)
          >>> place.add_insect(tank)
          >>> place.ant is tank
          True
          >>> bee = Bee(3)
          >>> place.add_insect(bee)
          >>> tank.action(colony)   # Both ants attack bee
          >>> bee.armor
          1
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
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing TankAnt action
          >>> tank = TankAnt()
          >>> place = colony.places['tunnel_0_1']
          >>> place.add_insect(tank)
          >>> for _ in range(3):
          ...     place.add_insect(Bee(1))
          >>> tank.action(colony)
          >>> len(place.bees)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Placement of ants
          >>> tank0 = TankAnt()
          >>> tank1 = TankAnt()
          >>> harvester0 = HarvesterAnt()
          >>> harvester1 = HarvesterAnt()
          >>> place0 = colony.places['tunnel_0_0']
          >>> place1 = colony.places['tunnel_0_1']
          >>> # Add tank before harvester
          >>> place0.add_insect(tank0)
          >>> place0.add_insect(harvester0)
          >>> colony.food = 0
          >>> tank0.action(colony)
          >>> colony.food
          1
          >>> for ant in [TankAnt(), HarvesterAnt()]:
          ...     try:
          ...         place0.add_insect(ant)
          ...     except AssertionError:
          ...         assert place0.ant is tank0,\
          ...                 'Tank was kicked out by {0}'.format(ant)
          ...         assert tank0.ant is harvester0,\
          ...                 'Contained ant was kicked out by {0}'.format(ant)
          ...         continue
          ...     assert False, 'No AssertionError raised when adding {0}'.format(ant)
          >>> # Add harvester before tank
          >>> place1.add_insect(harvester1)
          >>> place1.add_insect(tank1)
          >>> tank1.action(colony)
          >>> colony.food
          2
          >>> for ant in [TankAnt(), HarvesterAnt()]:
          ...     try:
          ...         place1.add_insect(ant)
          ...     except AssertionError:
          ...         assert place1.ant is tank1,\
          ...                 'Tank was kicked out by {0}'.format(ant)
          ...         assert tank1.ant is harvester1,\
          ...                 'Contained ant was kicked out by {0}'.format(ant)
          ...         continue
          ...     assert False, 'No AssertionError raised when adding {0}'.format(ant)
          >>> tank0.reduce_armor(tank0.armor)
          >>> place0.ant is harvester0
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Removing ants
          >>> tank = TankAnt()
          >>> test_ant = Ant()
          >>> place = Place('Test')
          >>> place.add_insect(tank)
          >>> place.add_insect(test_ant)
          >>> place.remove_insect(test_ant)
          >>> tank.ant is None
          True
          >>> test_ant.place is None
          True
          >>> place.remove_insect(tank)
          >>> place.ant is None
          True
          >>> tank.place is None
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> tank = TankAnt()
          >>> place = Place('Test')
          >>> place.add_insect(tank)
          >>> tank.action(colony) # Action without contained ant should not error
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
