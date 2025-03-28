def shortestPalindrome(s: str) -> str:
    rev = s[::-1]
    for i in range(len(s) + 1):
        if s.startswith(rev[i:]):
            return rev[:i] + s

def main():
    s = input()
    print(shortestPalindrome(s))

main()