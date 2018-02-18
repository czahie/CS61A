test = {
  'name': 'Problem 6',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'answer': 'create a cluster for each centroid consisting of all elements closest to that centroid.',
          'choices': [
            'randomly initialize k centroids',
            r"""
            create a cluster for each centroid consisting of all elements closest to
            that centroid.
            """,
            'find the centroid (average position) of each cluster.'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          What is the first step of the iterative portion of the
          k-means algorithm?
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
          >>> restaurants1 = [
          ...     make_restaurant('A', [-3, -4], [], 3, [make_review('A', 2)]),
          ...     make_restaurant('B', [1, -1],  [], 1, [make_review('B', 1)]),
          ...     make_restaurant('C', [2, -4],  [], 1, [make_review('C', 5)]),
          ... ]
          >>> centroids = k_means(restaurants1, 1)
          >>> centroids # should be 2-element lists of decimals
          [[0.0, -3.0]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> restaurants2 = [
          ...     make_restaurant('D', [2, 3], [], 2, [make_review('D', 2)]),
          ...     make_restaurant('E', [0, 3], [], 3, [make_review('E', 1)]),
          ... ]
          >>> centroids = k_means(restaurants2, 1)
          >>> centroids # should be 2-element lists of decimals
          [[1.0, 3.0]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> restaurants1 = [
          ...     make_restaurant('A', [-3, -4], [], 3, [make_review('A', 2)]),
          ...     make_restaurant('B', [1, -1], [],  1, [make_review('B', 1)]),
          ...     make_restaurant('C', [2, -4], [],  1, [make_review('C', 5)]),
          ... ]
          >>> centroids = k_means(restaurants1, 2)
          >>> centroids # should be 2-element lists of decimals
          [[-3.0, -4.0], [1.5, -2.5]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> cluster1 = [
          ...     make_restaurant('A', [-3, -4], [], 3, [make_review('A', 2)]),
          ... ]
          >>> cluster2 = [
          ...     make_restaurant('B', [1, -1], [], 1, [make_review('B', 1)]),
          ...     make_restaurant('C', [2, -4], [], 1, [make_review('C', 5)]),
          ...     make_restaurant('D', [2, 3],  [], 2, [make_review('D', 2)]),
          ...     make_restaurant('E', [0, 3],  [], 3, [make_review('E', 1)]),
          ...     make_restaurant('F', [-1, 0], [], 3, [make_review('F', 1)]),
          ...     make_restaurant('G', [4, 2],  [], 3, [make_review('E', 1)]),
          ... ]
          >>> restaurants = cluster1 + cluster2
          >>> centroids = k_means(restaurants, 2)
          >>> [[round(x, 5), round(y, 5)] for x, y in centroids]
          [[-3.0, -4.0], [1.33333, 0.5]]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import tests.test_functions as test
      >>> import recommend
      >>> old_sample = recommend.sample
      >>> test.swap_implementations(recommend)
      >>> recommend.sample = test.sample # deterministic sampling
      >>> make_review, make_restaurant = recommend.make_review, recommend.make_restaurant
      >>> k_means = recommend.k_means
      """,
      'teardown': r"""
      >>> recommend.sample = old_sample
      >>> test.restore_implementations(recommend)
      """,
      'type': 'doctest'
    }
  ]
}
