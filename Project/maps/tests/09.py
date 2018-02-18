test = {
  'name': 'Problem 9',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'answer': '85cc4d1eff44e1c6f45d86bf02942b8c',
          'choices': [
            'restaurant names',
            'restaurants',
            'restaurant ratings'
          ],
          'hidden': False,
          'locked': True,
          'question': 'rate_all returns a dictionary. What are the keys of this dictionary?'
        },
        {
          'answer': 'a9ca5d2f8f05a0b53223e921bc719c8d',
          'choices': [
            'numbers - a mix of user ratings and predicted ratings',
            'numbers - user ratings only',
            'numbers - predicted ratings only',
            'numbers - mean restaurant ratings',
            'lists - list of all restaurant ratings'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What are the values of the returned dictionary?'
        },
        {
          'answer': '18f4b8f373a149983a060187fb945841',
          'choices': [
            'a list of restaurants reviewed by the user',
            'a list of all possible restaurants',
            'a list of ratings for restaurants reviewed by the user'
          ],
          'hidden': False,
          'locked': True,
          'question': 'In rate_all, what does the variable reviewed represent?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> user = make_user('Mr. Mean Rating Minus One', [
          ...     make_review('A', 3),
          ...     make_review('B', 4),
          ...     make_review('C', 1),
          ... ])
          >>> cluster = [
          ...     make_restaurant('A', [1, 2], [], 4, [
          ...         make_review('A', 4),
          ...         make_review('A', 4)
          ...     ]),
          ...     make_restaurant('B', [4, 2], [], 3, [
          ...         make_review('B', 5)
          ...     ]),
          ...     make_restaurant('C', [-2, 6], [], 4, [
          ...         make_review('C', 2)
          ...     ]),
          ...     make_restaurant('D', [4, 4], [], 3.5, [
          ...         make_review('D', 2.5),
          ...         make_review('D', 3.5),
          ...     ]),
          ... ]
          >>> restaurants = {restaurant_name(r): r for r in cluster}
          >>> recommend.ALL_RESTAURANTS = cluster
          >>> to_rate = cluster[2:]
          >>> fns = [restaurant_price, lambda r: mean(restaurant_ratings(r))]
          >>> ratings = rate_all(user, to_rate, fns)
          >>> type(ratings)
          <class 'dict'>
          >>> len(ratings) # Only the restaurants passed to rate_all
          2
          >>> ratings['C'] # A restaurant rated by the user (should be an integer)
          1
          >>> round(ratings['D'], 5) # A predicted rating (should be a decimal)
          2.0
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import tests.test_functions as test
      >>> import recommend
      >>> from recommend import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> user = make_user('Mr. Mean Rating Minus One', [
          ...     make_review('A', 3),
          ...     make_review('B', 4),
          ...     make_review('C', 1),
          ... ])
          >>> cluster = [
          ...     make_restaurant('A', [1, 2], [], 4, [
          ...         make_review('A', 4),
          ...         make_review('A', 4)
          ...     ]),
          ...     make_restaurant('B', [4, 2], [], 3, [
          ...         make_review('B', 5)
          ...     ]),
          ...     make_restaurant('C', [-2, 6], [], 4, [
          ...         make_review('C', 2)
          ...     ]),
          ...     make_restaurant('D', [4, 4], [], 3.5, [
          ...         make_review('D', 2.5),
          ...         make_review('D', 3.5),
          ...     ]),
          ... ]
          >>> recommend.ALL_RESTAURANTS = cluster
          >>> to_rate = cluster[2:]
          >>> fns = [restaurant_price, lambda r: mean(restaurant_ratings(r))]
          >>> ratings = rate_all(user, to_rate, fns)
          >>> type(ratings)
          <class 'dict'>
          >>> len(ratings) # Only the restaurants passed to rate_all
          2
          >>> ratings['C'] # A restaurant rated by the user (should be an integer)
          1
          >>> round(ratings['D'], 5) # A predicted rating (should be a decimal)
          2.0
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import tests.test_functions as test
      >>> import recommend
      >>> test.swap_implementations(recommend)
      >>> from recommend import *
      """,
      'teardown': r"""
      >>> test.restore_implementations(recommend)
      """,
      'type': 'doctest'
    }
  ]
}
