test = {
  'name': 'skip_mul_ok',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'a4b8078cffcb4318519c4bb01f983419',
          'choices': [
            'The base case is flawed: it misses the case where n == 1',
            'The recursive case should be skip_mul(n - 1)',
            'The variable n does not change, causing a infinite loop',
            'None of the above'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Consider a function that returns the product of every other
          number from 1 to n:
          >>> skip_mul(5) # 5 * 3 * 1
          15
          >>> skip_mul(8) # 8 * 6 * 4 * 2
          384
          
          And here's how we define it:
          def skip_mul(n):
              if n == 2:
                  return 2
              else:
                  return n * skip_mul(n - 2)
          
          What is wrong with this definition?
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
