#문제: string 에서 같은 k 개의 연속된 알파벳들을 제거하여라

def removeDuplicates2(s: str, k: int) -> str:
    stack = []
    count_stack = []

    for c in s:
        if len(stack) == 0:
            stack.append(c)
            count_stack.append(1)

        elif stack[-1] == c:
            dup_count = count_stack[-1]
            if dup_count < k - 1:
                stack.append(c)
                count_stack.append(dup_count + 1)
            elif dup_count == k - 1:
                for _ in range(k - 1):
                    stack.pop()
                    count_stack.pop()

        else:
            stack.append(c)
            count_stack.append(1)

    return ''.join(stack)

print(removeDuplicates2(s='abbcddde',k=3))