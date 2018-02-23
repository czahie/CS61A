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
          c9452203eb0b0f0bd2454586a6c2fc5c
          # locked
          >>> StunThrower.food_cost
          50ae32be3e31df6c59633df7fdfb3a72
          # locked
          >>> slow.armor
          d89cf7c79d5a479b0f636734143ed5e6
          # locked
          >>> stun.armor
          d89cf7c79d5a479b0f636734143ed5e6
          # locked
          """,
          'hidden': False,
          'locked': True
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
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          """,
          'hidden': False,
          'locked': True
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
          7f44338412808161209e944b1ee0f78c
          # locked
          >>> bee2.place.name
          8344c19df8015306b462119efc8419cb
          # locked
          
          >>> bee1.action(colony)
          >>> bee2.action(colony)
          
          >>> bee1.place.name
          3790e10c482a73d13ef2418977d50780
          # locked
          >>> bee2.place.name
          ba5c35f55ba3229d1eb021382d9d19c5
          # locked
          """,
          'hidden': False,
          'locked': True
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
          040b6ad98a7360eba8d493c250a9b82e
          # locked
          
          >>> colony.time = 1
          >>> bee.action(colony) # slowed thrice
          >>> bee.place.name
          040b6ad98a7360eba8d493c250a9b82e
          # locked
          
          >>> colony.time = 2
          >>> bee.action(colony) # slowed thrice
          >>> bee.place.name
          8344c19df8015306b462119efc8419cb
          # locked
          
          >>> colony.time = 3
          >>> bee.action(colony) # slowed twice
          >>> bee.place.name
          8344c19df8015306b462119efc8419cb
          # locked
          
          >>> colony.time = 4
          >>> bee.action(colony) # slowed twice
          >>> bee.place.name
          ba5c35f55ba3229d1eb021382d9d19c5
          # locked
          
          >>> colony.time = 5
          >>> bee.action(colony) # slowed once
          >>> bee.place.name
          ba5c35f55ba3229d1eb021382d9d19c5
          # locked
          
          >>> colony.time = 6
          >>> bee.action(colony) # slowed once
          >>> bee.place.name
          7f44338412808161209e944b1ee0f78c
          # locked
          
          >>> colony.time = 7
          >>> bee.action(colony) # status effects have worn off
          >>> slow.armor
          73b94a1326ae2e803c3421016112207b
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
