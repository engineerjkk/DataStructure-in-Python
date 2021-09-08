#문제: string 에서 같은 두개의 연속된 알파벳들을 제거하여라


def removeDuplicates(s: str) -> str:
    stack = []
    for c in s:
        if len(stack) == 0:
            stack.append(c)
        elif stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    return ''.join(stack)

print(removeDuplicates(s='abbcbbcdef'))