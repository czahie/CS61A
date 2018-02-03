test = {
  'name': 'Question 5',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'answer': 'While score0 and score1 are both less than goal',
          'choices': [
            'While score0 and score1 are both less than goal',
            'While at least one of score0 or score1 is less than goal',
            'While score0 is less than goal',
            'While score1 is less than goal'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          The variables score0 and score1 are the scores for both
          players. Under what conditions should the game continue?
          """
        },
        {
          'answer': 'strategy1(score1, score0)',
          'choices': [
            'strategy1(score1, score0)',
            'strategy1(score0, score1)',
            'strategy1(score1)',
            'strategy1(score0)'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          If strategy1 is Player 1's strategy function, score0 is
          Player 0's current score, and score1 is Player 1's current
          score, then which of the following demonstrates correct
          usage of strategy1?
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
          >>> #
          >>> # Play function stops at goal
          >>> s0, s1 = hog.play(always(5), always(3), score0=91, score1=10, dice=always_three)
          >>> s0
          106
          >>> s1
          10
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> #
          >>> # Goal score is not hardwired
          >>> s0, s1 = hog.play(always(5), always(5), goal=10, dice=always_three)
          >>> s0
          15
          >>> s1
          0
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hog
      >>> always_three = hog.make_test_dice(3)
      >>> always = hog.always_roll
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> #
          >>> # Goal edge case
          >>> s0, s1 = hog.play(always(4), always(3), score0=88, score1=20, dice=always_three)
          >>> s0
          20
          >>> s1
          100
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> #
          >>> # Player 1 win
          >>> s0, s1 = hog.play(always(4), always(4), score0=87, score1=88, dice=always_three)
          >>> s0
          99
          >>> s1
          100
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Check strategies are actually used correctly
          >>> strat0 = lambda score, opponent: opponent % 10
          >>> strat1 = lambda score, opponent: opponent // 10
          >>> s0, s1 = hog.play(strat0, strat1, score0=40, score1=92, dice=always_three)
          >>> s0
          101
          >>> s1
          73
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> #
          >>> # Swine swap applies during Player 1 turn
          >>> s0, s1 = hog.play(always(4), always(4), score0=42, score1=96, dice=always_three)
          >>> s0
          108
          >>> s1
          54
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> #
          >>> # Free bacon refers to correct opponent score
          >>> s0, s1 = hog.play(always(0), always(0), score0=11, score1=99, dice=always_three)
          >>> s0
          21
          >>> s1
          102
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> #
          >>> # Handle multiple turns with many swaps
          >>> s0, s1 = hog.play(always(0), always(0), goal=5, dice=always_three)
          >>> s0
          2
          >>> s1
          7
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hog
      >>> always_three = hog.make_test_dice(3)
      >>> always = hog.always_roll
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> tests.play_utils.check_play_function(hog)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> # Fuzz Testing
      >>> # Plays a lot of random games, and calculates a secret value.
      >>> # Failing this test means something is wrong, but you should
      >>> # look at other tests to see where the problem might be.
      >>> # Hint: make sure you're only calling take_turn once per turn!
      >>> #
      >>> import hog, importlib
      >>> importlib.reload(hog)
      >>> import tests.play_utils
      """,
      'teardown': r"""
      
      """,
      'type': 'doctest'
    }
  ]
}
