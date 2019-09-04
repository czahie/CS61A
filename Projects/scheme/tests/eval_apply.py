test = {
  'name': 'Understanding scheme.py',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'For a user-defined procedure only',
          'choices': [
            'For a user-defined procedure only',
            'For a primitive procedure only',
            'For either a user-defined or primitive procedure'
          ],
          'hidden': False,
          'locked': False,
          'question': 'When does scheme_apply call scheme_eval?'
        },
        {
          'answer': 'env.lookup(expr)',
          'choices': [
            'env.lookup(expr)',
            'expr.first',
            'scheme_symbolp(expr)',
            'SPECIAL_FORMS[first](rest, env)'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          What expression in the body of scheme_eval computes
          the value of a symbol?
          """
        },
        {
          'answer': 'SchemeError("cannot call: 1")',
          'choices': [
            'SchemeError("malformed list: (1)")',
            'SchemeError("cannot call: 1")',
            'AssertionError',
            'SchemeError("unknown identifier: 1")'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What exception should be raised for the expression (1)?'
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
