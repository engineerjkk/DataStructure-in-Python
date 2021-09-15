#문제: 주어진 두 string s와 t가 Anagram관계를 가지는지 판별하여라

def isAnagram(s: str, t: str) -> bool:
    table = {}

#key는 문자고 해당하는 count를 value에 저장한다. 똑같은 문자는 +1을 해준다.
    for c in s:
        count = table.get(c)
        if count is None:
            table[c] = 1
            continue

        table[c] += 1
#t에서 해당하는 문자를 table에서 찾아 value를 -1해준다. 만약 table에 해당하는 문자열이 없으면 false를 리턴해준다.
    for c in t:
        count = table.get(c)
        if count is None:
            return False
        table[c] -= 1
# 한번 더 체크
# value가 0이 아닌게 있으면 false를 리턴
    for key, value in table.items():
        if value != 0:
            return False

    return True

#O(n), O(1) or O(nlogn), O(1)

print(isAnagram(s="nocodeprogram",t="promodernacog"))