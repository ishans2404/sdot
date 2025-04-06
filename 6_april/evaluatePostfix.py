def evaluate_postfix(expression):
    stack = []
    operators = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a // b
    }
    tokens = expression.split()
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        elif token in operators:
            if len(stack) < 2:
                raise ValueError("Insufficient operands in the expression.")
            b = stack.pop()
            a = stack.pop()
            result = operators[token](a, b)
            stack.append(result)
        else:
            raise ValueError(f"Invalid token encountered: {token}")
    if len(stack) != 1:
        raise ValueError("The user input has too many values.")
    return stack.pop()

postfix_expr = input()
result = evaluate_postfix(postfix_expr)
print(result)