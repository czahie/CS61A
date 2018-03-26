test = {
  'name': 'Structure',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'tree(1, [tree(2), tree(3, [tree(5)]), tree(4)])',
          'choices': [
            'tree(1, [tree(2), tree(3, [tree(5)]), tree(4)])',
            'tree(1, (tree(2), tree(3, (tree(5))), tree(5)))',
            'tree(2, [tree(1, tree(3, tree(5)))], tree(4))',
            'tree(1, [tree(2), tree(3), tree(4)], tree(5))'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          Which constructor call creates the following tree structure?
              1
            / | \
           2  3  4
             /
            5
          """
        },
        {
          'answer': 'tree(3, [tree(6, [tree(2), tree(1)]), tree(2), tree(7)])',
          'choices': [
            'tree(3, [tree(6, [tree(2), tree(1)]), tree(2), tree(7)])',
            'tree(3, tree(6, [tree(2), tree(1)]), tree(2), tree(7))',
            'tree(3, [tree(6), [tree(2), tree(1)], tree(2), tree(7)])',
            'tree(3, tree(6), [tree(2), tree(1)], [tree(2), tree(7)])'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          Which constructor call creates the following tree structure?
                3
              / | \
             6  2  7
            / \
           2   1
          """
        },
        {
          'answer': '2',
          'choices': [
            '2',
            '3',
            '6',
            '7'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          How many branches does the following tree have?
                7
               / \
              2  4
             /|  |
            1 5  2
              |
              3
          """
        },
        {
          'answer': '6, 1, 5, 4',
          'choices': [
            '6, 1, 5',
            '6, 1, 5, 4',
            '7, 6, 1, 5, 4',
            'None of the above'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          Given the following tree structure, what are all the leaves?
                7
              / | \
             3  2  4
            /  /|
           6  1 5
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
