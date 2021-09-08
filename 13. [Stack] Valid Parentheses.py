def isValid(s):
    stack = []
    lookup = {")": "(", "}": "{", "]": "["}

    for p in s:
        if p in lookup.values():
            stack.append(p)
        elif stack and lookup[p] == stack[-1]:

            stack.pop()
        else:
            return False
    return stack == []

s = "()[]{}"

print(isValid(s))
#index : 0 1 2 3 4 5
#negative index : -5 -4 -3 -2 -1
