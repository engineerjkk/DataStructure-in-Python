#문제: s 로 주어진 str을 decoding 해서 return 하여라

def decodeString(s: str) -> str:
    stack = []
    num_stack = []

    cur_num = 0
    cur_str = ''
    for c in s:
        if c == '[':
            stack.append(cur_str)
            num_stack.append(cur_num)
            cur_str = ''
            cur_num = 0
            continue

        elif c == ']':
            prev_str = stack.pop()
            num = num_stack.pop()
            cur_str = prev_str + num * cur_str
            continue

        if c.isdigit():
            cur_num = cur_num * 10 + int(c)
        else:
            cur_str += c

    return cur_str

print(decodeString(s='a2[b2[ak]]'))

print(decodeString(s='23[a100[def]42[b]'))