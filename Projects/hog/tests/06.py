test = {
  'name': 'Question 6',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> #
          >>> def echo(s0, s1):
          ...     print(s0, s1)
          ...     return echo
          >>> s0, s1 = play(always_roll(0), always_roll(0), goal=2, say=echo)
          1 0
          1 2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> #
          >>> # Ensure that say is properly updated within the body of play.
          >>> def total(s0, s1):
          ...     print(s0 + s1)
          ...     return echo
          >>> def echo(s0, s1):
          ...     print(s0, s1)
          ...     return total
          >>> s0, s1 = play(always_roll(0), always_roll(0), goal=7, say=echo)
          1 0
          3
          2 4
          9
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import play, always_roll
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> #
          >>> def echo_0(s0, s1):
          ...     print('*', s0)
          ...     return echo_0
          >>> def echo_1(s0, s1):
          ...     print('**', s1)
          ...     return echo_1
          >>> s0, s1 = play(always_roll(0), always_roll(0), goal=1, say=both(echo_0, echo_1))
          * 1
          ** 0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> #
          >>> s0, s1 = play(always_roll(0), always_roll(0), goal=10, say=both(say_scores, announce_lead_changes()))
          Player 0 now has 1 and Player 1 now has 0
          Player 0 takes the lead by 1
          Player 0 now has 1 and Player 1 now has 2
          Player 1 takes the lead by 1
          Player 0 now has 2 and Player 1 now has 4
          Player 0 now has 2 and Player 1 now has 7
          Player 0 now has 10 and Player 1 now has 7
          Player 0 takes the lead by 3
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import play, always_roll, both, announce_lead_changes, say_scores
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
