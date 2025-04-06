def longestValidParentheses(s):
    stk = [-1]
    maxLen = 0
    for i, c in enumerate(s):
        if c == '(':
            stk.append(i)
        else:
            stk.pop()
            if not stk:
                stk.append(i)
            else:
                maxLen = max(maxLen, i - stk[-1])
    return maxLen

s = input()
res = longestValidParentheses(s)
print(res)