test = {
  'name': 'Problem 11',
  'points': 4,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing BodyguardAnt parameters
          >>> bodyguard = BodyguardAnt()
          >>> BodyguardAnt.food_cost
          c9452203eb0b0f0bd2454586a6c2fc5c
          # locked
          >>> bodyguard.armor
          20d533d3e06345c8bd7072212867f2d1
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing container attributes
          >>> bodyguard = BodyguardAnt()
          >>> print(bodyguard.ant)
          044ef3c0c6fd739b6260fe6f6cae71dd
          # locked
          >>> bodyguard.container
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          >>> test_ant = Ant()
          >>> test_ant.container
          03456a09f22295a39ca84d133a26f63d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing contain_ant
          >>> bodyguard = BodyguardAnt()
          >>> bodyguard2 = BodyguardAnt()
          >>> test_ant = Ant()
          >>> test_ant2 = Ant()
          >>> bodyguard.can_contain(bodyguard2)
          03456a09f22295a39ca84d133a26f63d
          # locked
          >>> bodyguard.can_contain(test_ant)
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          >>> test_ant.can_contain(bodyguard)
          03456a09f22295a39ca84d133a26f63d
          # locked
          >>> bodyguard.contain_ant(test_ant)
          >>> bodyguard.ant is test_ant
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          >>> bodyguard.can_contain(test_ant2)
          03456a09f22295a39ca84d133a26f63d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Placing ants
          >>> colony.food = 0
          >>> bodyguard0 = BodyguardAnt()
          >>> harvester0 = HarvesterAnt()
          >>> place0 = colony.places['tunnel_0_0']
          >>> # Add bodyguard before harvester
          >>> place0.add_insect(bodyguard0)
          >>> place0.add_insect(harvester0)
          >>> place0.ant is bodyguard0
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          >>> bodyguard0.ant is harvester0
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          >>> bodyguard0.action(colony)
          >>> colony.food
          d89cf7c79d5a479b0f636734143ed5e6
          # locked
          >>> bodyguard0.reduce_armor(bodyguard0.armor)
          >>> place0.ant is harvester0
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          >>> bodyguard1 = BodyguardAnt()
          >>> harvester1 = HarvesterAnt()
          >>> place1 = colony.places['tunnel_0_1']
          >>> # Add harvester before bodyguard
          >>> place1.add_insect(harvester1)
          >>> place1.add_insect(bodyguard1)
          >>> place1.ant is bodyguard1
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          >>> bodyguard1.ant is harvester1
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          >>> bodyguard1.action(colony)
          >>> colony.food
          20d533d3e06345c8bd7072212867f2d1
          # locked
          >>> bodyguard1.reduce_armor(bodyguard1.armor)
          >>> place1.ant is harvester1
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Removing ants
          >>> bodyguard = BodyguardAnt()
          >>> test_ant = Ant()
          >>> place = Place('Test')
          >>> place.add_insect(bodyguard)
          >>> place.add_insect(test_ant)
          >>> place.remove_insect(test_ant)
          >>> print(bodyguard.ant)
          044ef3c0c6fd739b6260fe6f6cae71dd
          # locked
          >>> print(test_ant.place)
          044ef3c0c6fd739b6260fe6f6cae71dd
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Placement of ants
          >>> bodyguard0 = BodyguardAnt()
          >>> bodyguard1 = BodyguardAnt()
          >>> harvester0 = HarvesterAnt()
          >>> harvester1 = HarvesterAnt()
          >>> place0 = colony.places['tunnel_0_0']
          >>> place1 = colony.places['tunnel_0_1']
          >>> # Add bodyguard before harvester
          >>> place0.add_insect(bodyguard0)
          >>> place0.add_insect(harvester0)
          >>> colony.food = 0
          >>> bodyguard0.action(colony)
          >>> colony.food
          1
          >>> for ant in [BodyguardAnt(), HarvesterAnt()]:
          ...     try:
          ...         place0.add_insect(ant)
          ...     except AssertionError:
          ...         assert place0.ant is bodyguard0,\
          ...                 'Bodyguard was kicked out by {0}'.format(ant)
          ...         assert bodyguard0.ant is harvester0,\
          ...                 'Contained ant was kicked out by {0}'.format(ant)
          ...         continue
          ...     assert False, 'No AssertionError raised when adding {0}'.format(ant)
          >>> # Add harvester before bodyguard
          >>> place1.add_insect(harvester1)
          >>> place1.add_insect(bodyguard1)
          >>> bodyguard1.action(colony)
          >>> colony.food
          2
          >>> for ant in [BodyguardAnt(), HarvesterAnt()]:
          ...     try:
          ...         place1.add_insect(ant)
          ...     except AssertionError:
          ...         assert place1.ant is bodyguard1,\
          ...                 'Bodyguard was kicked out by {0}'.format(ant)
          ...         assert bodyguard1.ant is harvester1,\
          ...                 'Contained ant was kicked out by {0}'.format(ant)
          ...         continue
          ...     assert False, 'No AssertionError raised when adding {0}'.format(ant)
          >>> bodyguard0.reduce_armor(bodyguard0.armor)
          >>> place0.ant is harvester0
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Removing ants
          >>> bodyguard = BodyguardAnt()
          >>> test_ant = Ant()
          >>> place = Place('Test')
          >>> place.add_insect(bodyguard)
          >>> place.add_insect(test_ant)
          >>> place.remove_insect(test_ant)
          >>> bodyguard.ant is None
          True
          >>> place.remove_insect(bodyguard)
          >>> place.ant is None
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
    },
    {
      'cases': [
        {
          'code': r"""
          >>> bodyguard = BodyguardAnt()
          >>> bodyguard.action(colony) # Action without contained ant should not error
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing bodyguard performs thrower's action
          >>> bodyguard = BodyguardAnt()
          >>> thrower = ThrowerAnt()
          >>> bee = Bee(2)
          >>> # Place bodyguard before thrower
          >>> colony.places["tunnel_0_0"].add_insect(bodyguard)
          >>> colony.places["tunnel_0_0"].add_insect(thrower)
          >>> colony.places["tunnel_0_3"].add_insect(bee)
          >>> bodyguard.action(colony)
          >>> bee.armor
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing bodyguard performs thrower's action
          >>> bodyguard = BodyguardAnt()
          >>> thrower = ThrowerAnt()
          >>> bee = Bee(2)
          >>> # Place thrower before bodyguard
          >>> colony.places["tunnel_0_0"].add_insect(thrower)
          >>> colony.places["tunnel_0_0"].add_insect(bodyguard)
          >>> colony.places["tunnel_0_3"].add_insect(bee)
          >>> bodyguard.action(colony)
          >>> bee.armor
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing removing a bodyguard doesn't remove contained ant
          >>> place = colony.places['tunnel_0_0']
          >>> bodyguard = BodyguardAnt()
          >>> test_ant = Ant(1)
          >>> place.add_insect(bodyguard)
          >>> place.add_insect(test_ant)
          >>> colony.remove_ant('tunnel_0_0')
          >>> place.ant is test_ant
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing bodyguarded ant keeps instance attributes
          >>> test_ant = Ant()
          >>> def new_action(colony):
          ...     test_ant.armor += 9000
          >>> test_ant.action = new_action
          >>> place = colony.places['tunnel_0_0']
          >>> bodyguard = BodyguardAnt()
          >>> place.add_insect(test_ant)
          >>> place.add_insect(bodyguard)
          >>> place.ant.action(colony)
          >>> place.ant.ant.armor
          9001
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing if we can construct a container besides BodyGuard
          >>> ant = ThrowerAnt()
          >>> ant.container = True
          >>> ant.ant = None
          >>> ant.can_contain(ThrowerAnt())
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing container can contain a special non-container bodyguard
          >>> bodyguard = BodyguardAnt()
          >>> mod_guard = BodyguardAnt()
          >>> mod_guard.container = False
          >>> bodyguard.can_contain(mod_guard)
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
