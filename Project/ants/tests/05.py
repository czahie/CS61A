test = {
  'name': 'Problem 5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'answer': 'random_or_none, defined in ant.py',
          'choices': [
            'random_or_none, defined in ant.py',
            'random.random(), defined in the "random" module',
            'getitem, defined in the "operators" module'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          What function selects a random bee from a list of bees, or
          None, if an empty list is passed in?
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing nearest_bee
          >>> thrower = ThrowerAnt()
          >>> colony.places['tunnel_0_0'].add_insect(thrower)
          >>> place = colony.places['tunnel_0_0']
          >>> near_bee = Bee(2)
          >>> far_bee = Bee(2)
          >>> colony.places["tunnel_0_3"].add_insect(near_bee)
          >>> colony.places["tunnel_0_6"].add_insect(far_bee)
          >>> hive = colony.hive
          >>> thrower.nearest_bee(hive) is far_bee
          False
          >>> thrower.nearest_bee(hive) is near_bee
          True
          >>> thrower.action(colony)    # Attack!
          >>> near_bee.armor            # Should do 1 damage
          1
          >>> thrower.place is place    # Don't change self.place!
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing Nearest bee not in the hive
          >>> thrower = ThrowerAnt()
          >>> colony.places["tunnel_0_0"].add_insect(thrower)
          >>> hive = colony.hive
          >>> bee = Bee(2)
          >>> hive.add_insect(bee)      # Adding a bee to the hive
          >>> thrower.nearest_bee(hive) is bee
          False
          >>> thrower.action(colony)    # Attempt to attack
          >>> bee.armor                 # Bee armor should not change
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Test that ThrowerAnt attacks bees on its own square
          >>> thrower = ThrowerAnt()
          >>> colony.places['tunnel_0_0'].add_insect(thrower)
          >>> near_bee = Bee(2)
          >>> colony.places["tunnel_0_0"].add_insect(near_bee)
          >>> thrower.nearest_bee(colony.hive) is near_bee
          True
          >>> thrower.action(colony)   # Attack!
          >>> near_bee.armor           # should do 1 damage
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Test that ThrowerAnt attacks bees at end of tunnel
          >>> thrower = ThrowerAnt()
          >>> colony.places['tunnel_0_0'].add_insect(thrower)
          >>> near_bee = Bee(2)
          >>> colony.places["tunnel_0_8"].add_insect(near_bee)
          >>> thrower.nearest_bee(colony.hive) is near_bee
          True
          >>> thrower.action(colony)   # Attack!
          >>> near_bee.armor           # should do 1 damage
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing ThrowerAnt chooses a random target
          >>> thrower = ThrowerAnt()
          >>> colony.places["tunnel_0_0"].add_insect(thrower)
          >>> bee1 = Bee(1001)
          >>> bee2 = Bee(1001)
          >>> colony.places["tunnel_0_3"].add_insect(bee1)
          >>> colony.places["tunnel_0_3"].add_insect(bee2)
          >>> # Throw 1000 times. The first bee should take ~1000*1/2 = ~500 damage,
          >>> # and have ~501 remaining.
          >>> for _ in range(1000):
          ...     thrower.action(colony)
          >>> # Test if damage to bee1 is within 6 standard deviations (~95 damage)
          >>> # If bees are chosen uniformly, this is true 99.9999998% of the time.
          >>> def dmg_within_tolerance():
          ...     return abs(bee1.armor-501) < 95
          >>> dmg_within_tolerance()
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
