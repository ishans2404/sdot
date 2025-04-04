def count_substrings(s):
    count = 0
    last_seen = {'a': -1, 'b': -1, 'c': -1}
    for i, char in enumerate(s):
        if char in last_seen:
            last_seen[char] = i
            count += 1 + min(last_seen.values())
    return count

# User input
s = input("Enter a string containing 'a', 'b', 'c' only: ")
print("Number of substrings containing all three characters:", count_substrings(s))
