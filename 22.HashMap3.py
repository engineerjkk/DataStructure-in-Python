#문제: 주어진 두 string s와 t가 isomorphic 관계인지 찾아서 return하여라

def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    str_length = len(s)

    table1 = {}
    table2 = {}
    for idx in range(0, str_length):
        match1 = table1.get(s[idx]) #get(x) 함수는 x라는 Key에 대응되는 Value를 돌려준다.
        match2 = table2.get(t[idx])
        if match1 is None and match2 is None:
            table1[s[idx]] = t[idx] #value 넣기
            table2[t[idx]] = s[idx]
            continue

        elif match1 == t[idx] and match2 == s[idx]:
            continue

        return False


    return True

print(isIsomorphic(s="aaaccd", t="xxxyyz"))

'''
딕셔너리에 value 넣기
a={}
a["abc"]=1
a["abc"]=2
print(a)
'abc':2
'''