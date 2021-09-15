#문제: 주어진 string s에서, 가장 긴 palindromic substring을 return하여라
# abcba와같이 앞에서 읽을때와 뒤에서 읽을때가 같은 경우를 palindromic 이라고 한다.
def longestPalindrome(s: str) -> str:
    str_length = len(s)
    dp_table = [[0] * str_length for i in range(str_length)]

    for idx in range(str_length):
        dp_table[idx][idx] = 1

    for idx in range(str_length - 1):
        start_char = s[idx]
        end_char = s[idx + 1]
        if start_char == end_char:
            dp_table[idx][idx + 1] = 2

    for idx in range(2, str_length):
        row = 0
        col = idx
        while col < str_length:
            start_char = s[row]
            end_char = s[col]
            prev_count = dp_table[row + 1][col - 1]
            if start_char == end_char and prev_count != 0:
                dp_table[row][col] = prev_count + 2
            row += 1
            col += 1

    max_length = 0
    start_idx = 0
    end_idx = 0
    for row in range(str_length):
        for col in range(str_length):
            crnt_length = dp_table[row][col]
            if max_length < crnt_length:
                max_length = crnt_length
                start_idx = row
                end_idx = col

    sub_str = s[start_idx:end_idx + 1]

    return sub_str

#print(longestPalindrome(s='baabc'))