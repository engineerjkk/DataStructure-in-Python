#날자에 따른 온도가 temperatures 리스트로 주어진다. 이 때 해당 날짜에서부터 다음 따뜻한날까지의 차이를 가진 list를 return하여라

from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    temp_count = len(temperatures)
    ans = [0] * temp_count

    stack = []
    idx_stack = []

    for idx in range(temp_count - 1, -1, -1):
        temperature = temperatures[idx]

        last_temp_idx = 0
        while stack:
            last_temp = stack[-1]
            last_temp_idx = idx_stack[-1]
            if last_temp <= temperature:
                stack.pop()
                idx_stack.pop()
            else:
                break

        if len(stack) == 0:
            stack.append(temperature)
            idx_stack.append(idx)
            ans[idx] = 0
            continue

        stack.append(temperature)
        idx_stack.append(idx)
        ans[idx] = last_temp_idx - idx

    return ans

print(dailyTemperatures(temperatures=[39, 20, 70, 36, 30, 60, 80, 1]))