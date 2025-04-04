def combination_sum(candidates, target):
    result = []
    candidates.sort()
    def backtrack(start, path, total):
        if total == target:
            result.append(path[:])
            return
        if total > target:
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, total + candidates[i])
            path.pop()
    backtrack(0, [], 0)
    return result

n = int(input())
candidates = list(map(int, input().strip().split()))
target = int(input())
combinations = combination_sum(candidates, target)
combinations = sorted([sorted(comb) for comb in combinations])
for comb in combinations:
    print(" ".join(map(str, comb)))