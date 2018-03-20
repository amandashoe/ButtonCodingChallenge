"""
Module for expression evaluation

This module provides a function that implements an expression evaluator.
It accepts an expression as a space delimited string as input and returns the result.

Rules:
1. Expressions can be numbers or operator expressions (4 is an expression and so is - 3 1)
2. Numbers evaluate to themselves (4 is 4)
3. Operator expressions evaluate to an arithmetic computation of the two following sub-expressions.
Which arithmetic computation we make is determined by the first token in the operator expression.
The syntax is always <Operator> <Expression> <Expression>, so in + 1 2, + is the operator
and 1 and 2 are the expressions to sum.
4. The two operator types supported are + a b (evaluated as a + b) and - (evaluated as a - b)

Amanda Xu 
3/20/18
"""

def expEval(s):
    """Returns: Integer value of the evaluated expression in string s.

    Parameter s: the string with expression to evaluate
    Precondition: s is a space delimited string with a valid expression containing only
    operators +, - and integer numbers"""
    assert isinstance(s, str), "Must input string"
    assert len(s) > 0, "String cannot be empty"
    
    num = None
    
    while s!=str(num):
        sub = s[len(s)-5:].split()
        if sub[0] == "+":
            num = int(sub[1]) + int(sub[2])
        else:
            num = int(sub[1]) - int(sub[2])
        s = s[:len(s)-5] + str(num)
    return num
    
        
        
    