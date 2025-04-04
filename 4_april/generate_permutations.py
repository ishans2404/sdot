def backtrack(nums, path, used, result):
    if len(path) == len(nums):
        result.append("".join(path) if isinstance(nums, str) else list(path))
        return
    for i in range(len(nums)):
        if not used[i]:  
            used[i] = True
            path.append(nums[i])
            backtrack(nums, path, used, result)
            path.pop()  
            used[i] = False

def generate_permutations(elements):
    result = []
    used = [False] * len(elements)
    backtrack(elements, [], used, result)
    return result

user_input = input().strip()
if user_input.startswith("[") and user_input.endswith("]"):
    elements = list(map(int, user_input[1:-1].replace(" ", "").split(",")))
else:
    elements = list(user_input)
permutations = generate_permutations(elements)
for perm in permutations:
    print(perm)
