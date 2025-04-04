def check_rotated_string(s1: str, s2: str):
    combined_str = s1 + s1
    n, m = len(combined_str), len(s2)
    for i in range(n - m):
        if combined_str[i:i+m] == s2:
            print("string2 is a rotation of string1")
            return
    print("string2 is not a rotation of string1")

s1, s2 = input(), input()
check_rotated_string(s1, s2)