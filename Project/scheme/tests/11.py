test = {
  'name': 'Problem 11',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> frame = global_frame.make_child_frame(Pair('a', Pair('b', Pair('c', nil))), Pair(1, Pair(2, Pair(3, nil))))
          >>> global_frame.lookup('a') # Type SchemeError if you think this errors
          87c30138f7979b4f5a454aacfb191b98
          # locked
          >>> frame.lookup('a') # Type SchemeError if you think this errors
          2894dd5fa65c8aa8f2b9d920d0e542e0
          # locked
          >>> frame.lookup('b') # Type SchemeError if you think this errors
          e56af2bab40778990634a527fe4407f8
          # locked
          >>> frame.lookup('c') # Type SchemeError if you think this errors
          a3d16f1c59cdc683d6ce640b10aa5c1d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> frame = global_frame.make_child_frame(nil, nil)
          >>> frame.parent is global_frame
          a87b4aa619df2eba30bc86785b816612
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> first = Frame(global_frame)
          >>> second = first.make_child_frame(nil, nil)
          >>> second.parent is first
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme import *
      >>> global_frame = create_global_frame()
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # More argument values than formal parameters
          >>> global_frame.make_child_frame(Pair('a', nil), Pair(1, Pair(2, Pair(3, nil))))
          SchemeError
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # More formal parameters than argument values
          >>> global_frame.make_child_frame(Pair('a', Pair('b', Pair('c', nil))), Pair(1, nil))
          SchemeError
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Values can be pairs.
          >>> frame = global_frame.make_child_frame(Pair('a', Pair('b', nil)), Pair(Pair(1, nil), Pair(Pair(2, nil), nil)))
          >>> frame.lookup('a')
          Pair(1, nil)
          >>> frame.lookup('b')
          Pair(2, nil)
          >>> frame2 = frame.make_child_frame(nil, nil) # Bind parents correctly
          >>> frame2.lookup('a')
          Pair(1, nil)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme import *
      >>> global_frame = create_global_frame()
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
