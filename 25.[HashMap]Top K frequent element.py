#문제: 주어진 두 string s와 t가 Anagram관계를 가지는지 판별하여라
# 가장 많이 반복되는 k개 출력
from typing import List
import heapq


def topKFrequent(nums: List[int], k: int) -> List[int]:

    #해시 테이블 만들기 -> key 개수를 value에 저장한다.
    table = {}
    for num in nums:
        count = table.get(num)
        if count is None:
            table[num] = 0
        table[num] += 1

    # heap
    freq_heap = []
    for num, count in table.items():
        heapq.heappush(freq_heap, (count, num))
        if k < len(freq_heap):
            heapq.heappop(freq_heap)

    k_freq = []
    while freq_heap:
        count, num = freq_heap[0]
        heapq.heappop(freq_heap)
        k_freq.append(num)
    k_freq.reverse()

    return k_freq

print(topKFrequent(nums=[1,1,1,1,3,3,3,5,5,2,2,4,6], k=2))

# 가장 많이 반복되는 문자를 k개 출력한다. 그에 해당하는 key값 즉 숫자를 return하는 문제이다.
# 먼저 각 key에 해당하는 값이 몇번 반복되는지 value에 저장한다.
# 그리고 다시 어레이를 만들어 value에 따라 sorting을 한다.
# 그리고 2 초과하는 key를 만들어낸다.

# 해쉬맵의 value값으로 새로운 어레이에 key값을 정렬해준다.