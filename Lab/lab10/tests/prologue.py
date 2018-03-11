test = {
  'name': 'Prologue',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'Turns input into tokens',
          'choices': [
            'Turns input into tokens',
            'Tries to beat Superman',
            'Organizes tokens in a data structure',
            'Makes sure that there are no parentheses errors'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What does the lexer do?'
        },
        {
          'answer': 'Organizes tokens in a data structure',
          'choices': [
            'Turns input into tokens',
            'Organizes tokens in a data structure',
            'Evaluates the input',
            'Print the result of evaluation'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What does the parser do?'
        },
        {
          'answer': 'Read-Eval-Print-Loop',
          'choices': [
            'Read-Eval-Print-Loop',
            'Really-Enormous-Purple-Llamas',
            'Read-Eval-Parse-Lex'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What does REPL stand for?'
        },
        {
          'answer': 'literal, name, call expression, lambda expression',
          'choices': [
            'literal, name, call expression, lambda expression',
            'number, lambda function, primitive function, string',
            'value, expression, function, number',
            'name, function, number, literal'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What are all the types of expressions in PyCombinator?'
        },
        {
          'answer': 'number, lambda function, primitive function',
          'choices': [
            'number, lambda function, primitive function',
            'number, string, function',
            'name, number, lambda function',
            'number, lambda expression, primitive function'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What are all the types of values in PyCombinator?'
        },
        {
          'answer': 'a Number',
          'choices': [
            'a Number',
            'a String',
            'a Function',
            'an Expression'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What does a Literal evaluate to?'
        },
        {
          'answer': 'A lambda function is the result of evaluating a lambda expression',
          'choices': [
            'They are the same thing',
            'A lambda expression is the result of evaluating a lambda function',
            'A lambda function is the result of evaluating a lambda expression',
            'A lambda expression is a call to a lambda function'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What is the difference between a lambda expression and a lambda function?'
        },
        {
          'answer': 'A method of Expr objects that evaluates the Expr and returns a Value',
          'choices': [
            'A method of Expr objects that evaluates the Expr and returns a Value',
            'A method of Expr objects that evaluates a call expression and returns a Number',
            'A method of LambdaExpression objects that evaluates a function call',
            'A method of Literal objects that returns a Name'
          ],
          'hidden': False,
          'locked': False,
          'question': 'Which of the following describes the eval method?'
        },
        {
          'answer': 'As dictionaries that map variable names (strings) to Value objects',
          'choices': [
            'As dictionaries that map variable names (strings) to Value objects',
            'As sequences of Frame objects',
            'As dictionaries that map Name objects to Value objects',
            'As linked lists containing dictionaries'
          ],
          'hidden': False,
          'locked': False,
          'question': 'How are environments represented in our interpreter?'
        },
        {
          'answer': 'Literal(1)',
          'choices': [
            'Literal(1)',
            'Number(1)',
            "Name('1')",
            'Name(1)'
          ],
          'hidden': False,
          'locked': False,
          'question': "What will read('1') output?"
        },
        {
          'answer': "Name('x')",
          'choices': [
            'Literal(x)',
            'x',
            'Name(x)',
            "Name('x')"
          ],
          'hidden': False,
          'locked': False,
          'question': "What will read('x') output?"
        },
        {
          'answer': "CallExpr(Name('add'), [Literal(3), Literal(4)])",
          'choices': [
            "CallExpr(Literal('add'), Literal(3), Literal(4))",
            "CallExpr('add', [Literal(3), Literal(4)])",
            "CallExpr(Name('add'), Literal(3), Literal(4))",
            "CallExpr(Name('add'), [Literal(3), Literal(4)])"
          ],
          'hidden': False,
          'locked': False,
          'question': "What will read('add(3, 4)') output?"
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
