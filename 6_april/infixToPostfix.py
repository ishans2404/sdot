def infixToPostfix(infix):
    postfix = []
    stk = []
    for c in infix:
        if c.isalnum():
            postfix.append(c)
        elif c == '(':
            stk.append(c)
        elif c == ')':
            while stk and stk[-1] != '(':
                postfix.append(stk.pop())
            stk.pop()
        else:
            while stk and prec(c) <= prec(stk[-1]):
                postfix.append(stk.pop())
            stk.append(c)
    while stk:
        postfix.append(stk.pop())
    return ''.join(postfix)

def prec(op):
    if op in ('+', '-'):
        return 1
    elif op in ('*', '/'):
        return 2
    return -1

infix = input()
res = infixToPostfix(infix)
print(res)