test = {
  'name': 'factorial_ok',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': '110c41012168b28dee9e181a50429e77',
          'choices': [
            'The return statement in the recursive case is missing',
            'The base case is flawed: it should be n <= 0',
            'The recursive call is not combined correctly into the final solution',
            'The variable n does not change, causing a infinite loop'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Consider this implementation of the factorial function:
          def factorial(n):
              if n == 0:
                  return 1
              else:
                  return factorial(n-1)
          
          What is wrong with it?
          """
        }
      ],
      'scored': True,
      'type': 'concept'
    }
  ]
}
