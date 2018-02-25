test = {
  'name': 'Problem EC',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing status parameters
          >>> slow = SlowThrower()
          >>> stun = StunThrower()
          >>> SlowThrower.food_cost
          4
          >>> StunThrower.food_cost
          6
          >>> slow.armor
          1
          >>> stun.armor
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing Slow
          >>> slow = SlowThrower()
          >>> bee = Bee(3)
          >>> colony.places["tunnel_0_0"].add_insect(slow)
          >>> colony.places["tunnel_0_4"].add_insect(bee)
          >>> slow.action(colony)
          >>> colony.time = 1
          >>> bee.action(colony)
          >>> bee.place.name # SlowThrower should cause slowness on odd turns
          'tunnel_0_4'
          >>> colony.time += 1
          >>> bee.action(colony)
          >>> bee.place.name # SlowThrower should cause slowness on odd turns
          'tunnel_0_3'
          >>> for _ in range(3):
          ...    colony.time += 1
          ...    bee.action(colony)
          >>> bee.place.name
          'tunnel_0_1'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing Stun
          >>> error_msg = "StunThrower doesn't stun for exactly one turn."
          >>> stun = StunThrower()
          >>> bee = Bee(3)
          >>> colony.places["tunnel_0_0"].add_insect(stun)
          >>> colony.places["tunnel_0_4"].add_insect(bee)
          >>> stun.action(colony)
          >>> bee.action(colony)
          >>> bee.place.name # StunThrower should stun for exactly one turn
          'tunnel_0_4'
          >>> bee.action(colony)
          >>> bee.place.name # StunThrower should stun for exactly one turn
          'tunnel_0_3'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing if effects stack
          >>> stun = StunThrower()
          >>> bee = Bee(3)
          >>> stun_place = colony.places["tunnel_0_0"]
          >>> bee_place = colony.places["tunnel_0_4"]
          >>> stun_place.add_insect(stun)
          >>> bee_place.add_insect(bee)
          >>> for _ in range(4): # stun bee four times
          ...    stun.action(colony)
          
          >>> passed = True
          >>> for _ in range(4):
          ...    bee.action(colony)
          ...    if bee.place.name != 'tunnel_0_4':
          ...        passed = False
          
          >>> passed
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing multiple stuns
          >>> stun1 = StunThrower()
          >>> stun2 = StunThrower()
          >>> bee1 = Bee(3)
          >>> bee2 = Bee(3)
          
          >>> colony.places["tunnel_0_0"].add_insect(stun1)
          >>> colony.places["tunnel_0_1"].add_insect(bee1)
          >>> colony.places["tunnel_0_2"].add_insect(stun2)
          >>> colony.places["tunnel_0_3"].add_insect(bee2)
          
          >>> stun1.action(colony)
          >>> stun2.action(colony)
          >>> bee1.action(colony)
          >>> bee2.action(colony)
          
          >>> bee1.place.name
          'tunnel_0_1'
          >>> bee2.place.name
          'tunnel_0_3'
          
          >>> bee1.action(colony)
          >>> bee2.action(colony)
          
          >>> bee1.place.name
          'tunnel_0_0'
          >>> bee2.place.name
          'tunnel_0_2'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing long effect stack
          >>> stun = StunThrower()
          >>> slow = SlowThrower()
          >>> bee = Bee(3)
          >>> colony.places["tunnel_0_0"].add_insect(stun)
          >>> colony.places["tunnel_0_1"].add_insect(slow)
          >>> colony.places["tunnel_0_4"].add_insect(bee)
          >>> for _ in range(3): # slow bee three times
          ...    slow.action(colony)
          
          >>> stun.action(colony) # stun bee once
          
          >>> colony.time = 0
          >>> bee.action(colony) # stunned
          >>> bee.place.name
          'tunnel_0_4'
          
          >>> colony.time = 1
          >>> bee.action(colony) # slowed thrice
          >>> bee.place.name
          'tunnel_0_4'
          
          >>> colony.time = 2
          >>> bee.action(colony) # slowed thrice
          >>> bee.place.name
          'tunnel_0_3'
          
          >>> colony.time = 3
          >>> bee.action(colony) # slowed twice
          >>> bee.place.name
          'tunnel_0_3'
          
          >>> colony.time = 4
          >>> bee.action(colony) # slowed twice
          >>> bee.place.name
          'tunnel_0_2'
          
          >>> colony.time = 5
          >>> bee.action(colony) # slowed once
          >>> bee.place.name
          'tunnel_0_2'
          
          >>> colony.time = 6
          >>> bee.action(colony) # slowed once
          >>> bee.place.name
          'tunnel_0_1'
          
          >>> colony.time = 7
          >>> bee.action(colony) # status effects have worn off
          >>> slow.armor
          0
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
