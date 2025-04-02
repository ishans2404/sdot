def longestPalindrome(s: str) -> str:
    if not s:
        return ""
    n = len(s)
    res = []
    def expand(l, r):
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1

    start, end = 0, 0
    for i in range(n):
        even = expand(i, i+1)
        odd = expand(i, i)
        maxi = max(even, odd)

        if maxi > end - start:
            start = i - (maxi - 1) // 2
            end = i + (maxi) // 2
        if not res:
            res.append(s[start : end+1])
        elif len(res[0]) < len(s[start : end+1]):
            res[0] = s[start : end+1]
    
    return res[0]

def main():
    s = input()
    res = longestPalindrome(s)
    print(res)

main()