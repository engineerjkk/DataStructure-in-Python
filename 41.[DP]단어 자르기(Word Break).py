#문제: 주어진 string s를 wordDict 만으로 만들 수 있는지 판별하여라

from typing import List


def wordBreak(s: str, wordDict: List[str]) -> bool:
    word_set = set()
    for word in wordDict:
        word_set.add(word)

    str_length = len(s)
    dp_arry = [False] * (str_length + 1)
    dp_arry[0] = True

    for idx in range(1, len(dp_arry)):
        for word in word_set:
            word_length = len(word)
            prev_idx = idx - word_length
            if prev_idx < 0:
                continue

            if dp_arry[prev_idx] == False:
                continue

            if s[prev_idx:idx] == word:
                dp_arry[idx] = True
                break

    return dp_arry[-1]  # return last elem

print(wordBreak(s='nocodeprogram', wordDict=['noc','cod','code','program']))
print(wordBreak(s='nocope', wordDict=['e','no','cop']))