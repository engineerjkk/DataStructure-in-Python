def stdStr(haystack:str,needle:str):
    if not needle:
        return 0
    for i in range(len(haystack)):
        if haystack[i:i+len(needle)]==needle:
            return i
    return -1

haystack="hello"
needle="ll"

answer=stdStr(haystack,needle)
print(answer)