#문제: s가 pattern에서의 패턴을 가지는지 판별하여라

def wordPattern(pattern: str, s: str) -> bool:
    char_map = {}
    word_map = {}

    words = s.split(' ')
    if len(words) != len(pattern):
        return False

    for idx, c in enumerate(pattern):
        word = words[idx]
        if c not in char_map:
            if word in word_map:
                return False

            else:
                char_map[c] = word
                word_map[word] = c

        else:
            if char_map[c] != word:
                return False

    return True

print(wordPattern(pattern="abba",s="banana apple apple banana"))

#O(n),O(1)