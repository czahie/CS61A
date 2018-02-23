test = {
  'name': 'Link',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from lab07 import *
          >>> link = Link(1, Link(2, Link(3)))
          >>> link.first
          1
          >>> link.rest.first
          2
          >>> link.rest.rest.rest is Link.empty
          True
          >>> link.first = 9001
          >>> link.first
          9001
          >>> link.rest = link.rest.rest
          >>> link.rest.first
          3
          >>> link = Link(1)
          >>> link.rest = link
          >>> link.rest.rest.rest.rest.first
          1
          >>> link = Link(2, Link(3, Link(4)))
          >>> link2 = Link(1, link)
          >>> link2.first
          1
          >>> link2.rest.first
          2
          >>> print(link2) # Look at the __str__ method of Link in lab07.py
          <1 2 3 4>
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
