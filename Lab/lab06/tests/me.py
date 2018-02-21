test = {
  'name': 'Me',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from data import *
          >>> type(me.name) == str
          True
          >>> me.place is sather_gate
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
