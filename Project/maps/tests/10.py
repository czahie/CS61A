test = {
  'name': 'Problem 10',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'answer': 'a list of strings (categories)',
          'choices': [
            'a list of strings (categories)',
            'a single string (category)',
            'a single number (rating)',
            'a list of numbers (ratings)'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          Given a restaurant, what does restaurant_categories in
          abstractions.py return?
          """
        },
        {
          'answer': "if the query string is one of the restaurant's categories",
          'choices': [
            "if the query string is a substring of the restaurant's name",
            "if the query string is mentioned in the restaurant's reviews",
            "if the query string is one of the restaurant's categories",
            "if the query string is equal to the restaurant's categories"
          ],
          'hidden': False,
          'locked': False,
          'question': 'When does a restaurant match a search query?'
        },
        {
          'answer': 'a list of restaurants',
          'choices': [
            'a list of restaurants',
            'a list of restaurant names (strings)',
            'a dictionary that maps restaurant names (strings) to restaurants',
            'a dictionary that maps restaurant categories (strings) to restaurants'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What type of object does search return?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> def make_testaurant(name, categories):
          ...     return make_restaurant(name, [0, 0], categories, 1, [
          ...         make_review(name, 5)
          ...     ])
          >>> a = make_testaurant('A', ['Creperies', 'Italian'])
          >>> b = make_testaurant('B', ['Italian', 'Coffee & Tea'])
          >>> c = make_testaurant('C', ['Coffee & Tea', 'Greek', 'Creperies'])
          >>> d = make_testaurant('D', ['Greek'])
          >>> test.check_same_elements(search('Creperies', [a, b, c, d]), [a, c])
          True
          >>> test.check_same_elements(search('Thai', [a, b, c, d]), [])
          True
          >>> test.check_same_elements(search('Coffee & Tea', [a, b, d]), [b])
          True
          >>> test.check_same_elements(search('Greek', [a, b, c, d]), [c, d])
          True
          >>> test.check_same_elements(search('Italian', [a, b, c, d]), [a, b])
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import tests.test_functions as test
      >>> import recommend
      >>> make_user, make_review, make_restaurant = recommend.make_user, recommend.make_review, recommend.make_restaurant
      >>> search = recommend.search
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> def make_testaurant(name, categories):
          ...     return make_restaurant(name, [0, 0], categories, 1, [
          ...         make_review(name, 5)
          ...     ])
          >>> a = make_testaurant('A', ['Creperies', 'Italian'])
          >>> b = make_testaurant('B', ['Italian', 'Coffee & Tea'])
          >>> c = make_testaurant('C', ['Coffee & Tea', 'Greek', 'Creperies'])
          >>> d = make_testaurant('D', ['Greek'])
          >>> test.check_same_elements(search('Creperies', [a, b, c, d]), [a, c])
          True
          >>> test.check_same_elements(search('Thai', [a, b, c, d]), [])
          True
          >>> test.check_same_elements(search('Coffee & Tea', [a, b, d]), [b])
          True
          >>> test.check_same_elements(search('Greek', [a, b, c, d]), [c, d])
          True
          >>> test.check_same_elements(search('Italian', [a, b, c, d]), [a, b])
          True
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
      >>> make_user, make_review, make_restaurant = recommend.make_user, recommend.make_review, recommend.make_restaurant
      >>> search = recommend.search
      """,
      'teardown': r"""
      >>> test.restore_implementations(recommend)
      """,
      'type': 'doctest'
    }
  ]
}
