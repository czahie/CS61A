test = {
  'name': 'Problem 13',
  'points': 4,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing QueenAnt parameters
          >>> ants.QueenAnt.food_cost
          7cd035adf49fc93a635b4e8bb2e28bd4
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # QueenAnt Placement
          >>> queen = ants.QueenAnt()
          >>> impostor = ants.QueenAnt()
          >>> front_ant, back_ant = ants.ThrowerAnt(), ants.ThrowerAnt()
          >>> tunnel = [colony.places['tunnel_0_{0}'.format(i)]
          ...         for i in range(9)]
          >>> tunnel[1].add_insect(back_ant)
          >>> tunnel[7].add_insect(front_ant)
          >>> tunnel[4].add_insect(impostor)
          >>> impostor.action(colony)
          >>> impostor.armor            # Impostors must die!
          73b94a1326ae2e803c3421016112207b
          # locked
          >>> tunnel[4].ant is None
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          >>> back_ant.damage           # Ants should not be buffed
          d89cf7c79d5a479b0f636734143ed5e6
          # locked
          >>> front_ant.damage
          d89cf7c79d5a479b0f636734143ed5e6
          # locked
          >>> tunnel[4].add_insect(queen)
          >>> queen.action(colony)
          >>> queen.armor               # Long live the Queen!
          d89cf7c79d5a479b0f636734143ed5e6
          # locked
          >>> back_ant.damage           # Ants behind queen should be buffed
          20d533d3e06345c8bd7072212867f2d1
          # locked
          >>> front_ant.damage
          d89cf7c79d5a479b0f636734143ed5e6
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # QueenAnt Removal
          >>> queen = ants.QueenAnt()
          >>> impostor = ants.QueenAnt()
          >>> place = colony.places['tunnel_0_2']
          >>> place.add_insect(impostor)
          >>> place.remove_insect(impostor)
          >>> place.ant is None         # Impostors can be removed
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          >>> place.add_insect(queen)
          >>> place.remove_insect(queen)
          >>> place.ant is queen        # True queen cannot be removed
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # QueenAnt knows how to swim
          >>> queen = ants.QueenAnt()
          >>> water = ants.Water('Water')
          >>> water.add_insect(queen)
          >>> queen.armor
          d89cf7c79d5a479b0f636734143ed5e6
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing damage multiplier
          >>> queen_tunnel, side_tunnel = [[colony.places['tunnel_{0}_{1}'.format(i, j)]
          ...         for j in range(9)] for i in range(2)]
          >>> queen = ants.QueenAnt()
          >>> back = ants.ThrowerAnt()
          >>> front = ants.ThrowerAnt()
          >>> guard = ants.BodyguardAnt()
          >>> guarded = ants.ThrowerAnt()
          >>> side = ants.ThrowerAnt()
          >>> bee = ants.Bee(10)
          >>> side_bee = ants.Bee(10)
          >>> queen_tunnel[0].add_insect(back)
          >>> queen_tunnel[1].add_insect(guard)
          >>> queen_tunnel[1].add_insect(guarded)
          >>> queen_tunnel[2].add_insect(queen)
          >>> queen_tunnel[3].add_insect(front)
          >>> side_tunnel[0].add_insect(side)
          >>> queen_tunnel[4].add_insect(bee)
          >>> side_tunnel[4].add_insect(side_bee)
          >>> queen.action(colony)
          >>> bee.armor
          8b5f7651e8464d241749041812e40bfa
          # locked
          >>> back.action(colony)
          >>> bee.armor
          7cd035adf49fc93a635b4e8bb2e28bd4
          # locked
          >>> front.action(colony)
          >>> bee.armor
          50ae32be3e31df6c59633df7fdfb3a72
          # locked
          >>> guard.action(colony)
          >>> bee.armor
          c9452203eb0b0f0bd2454586a6c2fc5c
          # locked
          >>> side.action(colony)
          >>> side_bee.armor
          8b5f7651e8464d241749041812e40bfa
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import ants, importlib
      >>> importlib.reload(ants)
      >>> hive = ants.Hive(ants.AssaultPlan())
      >>> dimensions = (2, 9)
      >>> colony = ants.AntColony(None, hive, ants.ant_types(),
      ...         ants.dry_layout, dimensions)
      >>> ants.bees_win = lambda: None
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing game over
          >>> queen = ants.QueenAnt()
          >>> impostor = ants.QueenAnt()
          >>> tunnel = [colony.places['tunnel_0_{0}'.format(i)]
          ...         for i in range(9)]
          >>> tunnel[4].add_insect(queen)
          >>> tunnel[6].add_insect(impostor)
          >>> bee = ants.Bee(3)
          >>> tunnel[6].add_insect(bee)     # Bee in place with impostor
          >>> bee.action(colony)            # Game should not end
          
          >>> bee.move_to(tunnel[4])        # Bee moved to place with true queen
          >>> bee.action(colony)            # Game should end
          BeesWinException
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing if queen will not crash with no one to buff
          >>> queen = ants.QueenAnt()
          >>> colony.places['tunnel_0_2'].add_insect(queen)
          >>> queen.action(colony)
          >>> # Attack a bee
          >>> bee = ants.Bee(3)
          >>> colony.places['tunnel_0_4'].add_insect(bee)
          >>> queen.action(colony)
          >>> bee.armor # Queen should still hit the bee
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing QueenAnt action method
          >>> queen = ants.QueenAnt()
          >>> impostor = ants.QueenAnt()
          >>> bee = ants.Bee(10)
          >>> ant = ants.ThrowerAnt()
          >>> colony.places['tunnel_0_0'].add_insect(ant)
          >>> colony.places['tunnel_0_1'].add_insect(queen)
          >>> colony.places['tunnel_0_2'].add_insect(impostor)
          >>> colony.places['tunnel_0_4'].add_insect(bee)
          
          >>> impostor.action(colony)
          >>> bee.armor   # Impostor should not damage bee
          10
          >>> ant.damage  # Impostor should not double damage
          1
          
          >>> queen.action(colony)
          >>> bee.armor   # Queen should damage bee
          9
          >>> ant.damage  # Queen should double damage
          2
          >>> ant.action(colony)
          >>> bee.armor   # If failed, ThrowerAnt has incorrect damage
          7
          
          >>> queen.armor   # Long live the Queen
          1
          >>> impostor.armor  # Short-lived impostor
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Extensive damage doubling tests
          >>> queen_tunnel, side_tunnel = [[colony.places['tunnel_{0}_{1}'.format(i, j)]
          ...         for j in range(9)] for i in range(2)]
          >>> queen = ants.QueenAnt()
          >>> queen_tunnel[7].add_insect(queen)
          >>> # Turn 0
          >>> thrower = ants.ThrowerAnt()
          >>> fire = ants.FireAnt()
          >>> ninja = ants.NinjaAnt()
          >>> side = ants.ThrowerAnt()
          >>> front = ants.NinjaAnt()
          >>> queen_tunnel[0].add_insect(thrower)
          >>> queen_tunnel[1].add_insect(fire)
          >>> queen_tunnel[2].add_insect(ninja)
          >>> queen_tunnel[8].add_insect(front)
          >>> side_tunnel[0].add_insect(side)
          >>> buffed_ants = [thrower, fire, ninja]
          >>> old_dmgs = [ant.damage for ant in buffed_ants]
          >>> queen.action(colony)
          >>> for ant, dmg in zip(buffed_ants, old_dmgs):
          ...     assert ant.damage == dmg * 2,\
          ...         "{0}'s damage is {1}, but should be {2}".format(ant, ant.damage, dmg * 2)
          >>> for ant in [side, front]:
          ...     assert ant.damage == dmg,\
          ...         "{0}'s damage is {1}, but should be {2}".format(ant, ant.damage, dmg)
          >>> assert queen.damage == 1,\
          ...     'QueenAnt damage was modified to {0}'.format(ant.damage)
          >>> # Turn 1
          >>> tank = ants.TankAnt()
          >>> guard = ants.BodyguardAnt()
          >>> queen_tank = ants.TankAnt()
          >>> queen_tunnel[6].add_insect(tank)          # Not protecting an ant
          >>> queen_tunnel[1].add_insect(guard)         # Guarding FireAnt
          >>> queen_tunnel[7].add_insect(queen_tank)    # Guarding QueenAnt
          >>> buffed_ants.extend([tank, guard])
          >>> old_dmgs.extend([ant.damage for ant in [tank, guard, queen_tank]])
          >>> queen.action(colony)
          >>> for ant, dmg in zip(buffed_ants, old_dmgs):
          ...     assert ant.damage == dmg * 2,\
          ...         "{0}'s damage is {1}, but should be {2}".format(ant, ant.damage, dmg * 2)
          >>> # Turn 2
          >>> thrower1 = ants.ThrowerAnt()
          >>> thrower2 = ants.ThrowerAnt()
          >>> queen_tunnel[6].add_insect(thrower1)      # Add thrower1 in TankAnt
          >>> queen_tunnel[5].add_insect(thrower2)
          >>> buffed_ants.extend([thrower1, thrower2])
          >>> old_dmgs.extend([ant.damage for ant in [thrower1, thrower2]])
          >>> queen.action(colony)
          >>> for ant, dmg in zip(buffed_ants, old_dmgs):
          ...     assert ant.damage == dmg * 2,\
          ...         "{0}'s damage is {1}, but should be {2}".format(ant, ant.damage, dmg * 2)
          >>> # Turn 3
          >>> tank.reduce_armor(tank.armor)             # Expose thrower1
          >>> queen.action(colony)
          >>> for ant, dmg in zip(buffed_ants, old_dmgs):
          ...     assert ant.damage == dmg * 2,\
          ...         "{0}'s damage is {1}, but should be {2}".format(ant, ant.damage, dmg * 2)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Adding/Removing QueenAnt with Container
          >>> queen = ants.QueenAnt()
          >>> impostor = ants.QueenAnt()
          >>> container = ants.TankAnt()
          >>> colony.places['tunnel_0_3'].add_insect(container)
          >>> colony.places['tunnel_0_3'].add_insect(impostor)
          >>> impostor.action(colony)
          >>> colony.places['tunnel_0_3'].ant is container
          True
          >>> container.place is colony.places['tunnel_0_3']
          True
          >>> container.ant is None
          True
          >>> impostor.place is None
          True
          >>> colony.places['tunnel_0_3'].add_insect(queen)
          >>> colony.places['tunnel_0_3'].remove_insect(queen)
          >>> container.ant is queen
          True
          >>> queen.place is colony.places['tunnel_0_3']
          True
          >>> queen.action(colony)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import ants, importlib
      >>> importlib.reload(ants)
      >>> hive = ants.Hive(ants.AssaultPlan())
      >>> dimensions = (2, 9)
      >>> colony = ants.AntColony(None, hive, ants.ant_types(),
      ...         ants.dry_layout, dimensions)
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
