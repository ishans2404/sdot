def LongestSubstringWithoutRepeatingChars(s: str):
    res = 0
    left = 0
    seen = set()
    for right in range(len(s)):
        while s[right] in seen:
            left += 1
            seen.remove(s[left])
        res = max(res, right - left + 1)
        seen.add(s[right])
    return res

def main():
    s = "xyzyyxz"
    res = LongestSubstringWithoutRepeatingChars(s)
    print(res)

main()