#문제: 주어진 String s에서 반복되지 않는 첫번째 character의 index를 return하여라

def firstUniqueChar(s: str) -> int:
    count = {}
    for c in s:
        crnt_count = count.get(c)
        if crnt_count is None:
            count[c] = 1
            continue
        count[c] += 1

    for idx, c in enumerate(s):
        if count[c] == 1:
            return idx

    return -1


print(firstUniqueChar(s="nownocodeprogram"))
