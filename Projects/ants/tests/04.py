test = {
  'name': 'Problem 4',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing FireAnt parameters
          >>> fire = FireAnt()
          >>> FireAnt.food_cost
          5
          >>> fire.armor
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing fire damage
          >>> place = colony.places['tunnel_0_4']
          >>> bee = Bee(5)
          >>> place.add_insect(bee)
          >>> place.add_insect(FireAnt())
          >>> bee.action(colony) # attack the FireAnt
          >>> bee.armor
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing fire does damage to all Bees in its Place
          >>> place = colony.places['tunnel_0_4']
          >>> place.add_insect(FireAnt())
          >>> for i in range(100):          # Add 100 Bees
          ...     place.add_insect(Bee(3))
          >>> place.bees[0].action(colony)  # Attack the FireAnt
          >>> len(place.bees)               # How many bees are left?
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing fire damage is instance attribute
          >>> place = colony.places['tunnel_0_4']
          >>> bee = Bee(900)
          >>> buffAnt = FireAnt()
          >>> buffAnt.damage = 500   # Feel the burn!
          >>> place.add_insect(bee)
          >>> place.add_insect(buffAnt)
          >>> bee.action(colony) # attack the FireAnt
          >>> bee.armor  # is damage an instance attribute?
          400
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # General FireAnt Test
          >>> place = colony.places['tunnel_0_4']
          >>> bee = Bee(10)
          >>> ant = FireAnt()
          >>> place.add_insect(bee)
          >>> place.add_insect(ant)
          >>> bee.action(colony)    # Attack the FireAnt
          >>> bee.armor
          7
          >>> ant.armor
          0
          >>> place.ant is None     # The FireAnt should not occupy the place anymore
          True
          >>> bee.action(colony)
          >>> bee.armor             # Bee should not get damaged again
          7
          >>> bee.place.name        # Bee should not have been blocked
          'tunnel_0_3'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # General FireAnt Test
          >>> place = colony.places['tunnel_0_4']
          >>> bee = Bee(10)
          >>> ant = FireAnt()
          >>> place.add_insect(bee)
          >>> place.add_insect(ant)
          >>> ant.reduce_armor(0.1) # Poke the FireAnt
          >>> bee.armor             # Bee should not get damaged
          10
          >>> ant.armor
          0.9
          >>> place.ant is ant      # The FireAnt should still be at place
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
