def longestHappyPrefix(s: str) -> str:
    res = ""
    for i in range(1, len(s)):
        if s[:i] == s[len(s) - i:]:
            res = s[:i]
    return res

def main():
    s ="level"
    res = longestHappyPrefix(s)
    print(res)
main()