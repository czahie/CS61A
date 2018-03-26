test = {
  'name': 'Link',
  'points': 0,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> from link import *
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
          >>> print_link(link2) # Look at print_link in link.py
          <1 2 3 4>
          """,
        },
      ]
    },
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> from link import *
          >>> link = Link(1, Link(2, Link(3)))
          >>> link.rest.rest = Link(5, Link(4))
          >>> link.rest.rest.first
          5
          >>> link.rest.rest.rest.rest is Link.empty
          True
          >>> link.rest.rest = link
          >>> link.rest.rest.rest.first
          2
          """,
        },
      ]
    }
  ]
}