def basic_calculator():
    expression = input().replace(" ", "")
    
    def precedence(op):
        if op in ('+', '-'):
            return 1
        if op in ('*', '/'):
            return 2
        return 0
    
    def apply_op(a, b, op):
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/': return a // b
    
    values = []
    ops = []
    i = 0
    
    while i < len(expression):
        if expression[i] == ' ':
            i += 1
            continue
        
        if expression[i] == '(':
            ops.append(expression[i])
            i += 1
        elif expression[i].isdigit():
            val = 0
            while i < len(expression) and expression[i].isdigit():
                val = val * 10 + int(expression[i])
                i += 1
            values.append(val)
        elif expression[i] == ')':
            while ops and ops[-1] != '(':
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.append(apply_op(val1, val2, op))
            ops.pop() 
            i += 1
        else:
            while ops and precedence(ops[-1]) >= precedence(expression[i]):
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.append(apply_op(val1, val2, op))
            ops.append(expression[i])
            i += 1
    
    while ops:
        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()
        values.append(apply_op(val1, val2, op))
    
    print( values[-1])

basic_calculator()