def count_substrings(s):
    count = 0
    last_seen = {'a': -1, 'b': -1, 'c': -1}
    for i, char in enumerate(s):
        if char in last_seen:
            last_seen[char] = i
            count += 1 + min(last_seen.values())
    return count

s = input()
print(count_substrings(s))
