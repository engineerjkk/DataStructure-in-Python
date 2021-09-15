#문제: O(1) random Return을 지원하는 hash Set을 구현하여라

import random
from typing import List


class RandomizedSet:
    def __init__(self):
        self._table = {}
        self._arry = []

    def insert(self, val: int) -> bool:
        idx = self._table.get(val)
        if idx is not None:
            return False

        idx = len(self._arry)
        self._arry.append(val)
        self._table[val] = idx
        return True

    def remove(self, val: int) -> bool:
        idx = self._table.get(val)
        if idx is None:
            return False

        last_val = self._arry[-1]
        self._arry[idx] = last_val
        self._table[last_val] = idx
        self._arry.pop()
        self._table.pop(val)

        return True

    def getRandom(self) -> int:
        return random.choice(self._arry)

randomSet = RandomizedSet()
print(randomSet.insert(3), end=' ')
print(randomSet.insert(5), end=' ')
print(randomSet.insert(7), end=' ')
print(randomSet.insert(8), end=' ')
print(randomSet.insert(7), end=' ')
print(randomSet.getRandom(), end=' ')
print(randomSet.remove(5), end=' ')
print(randomSet.remove(3), end=' ')
print(randomSet.getRandom(), end=' ')


'''
O(1) inset
O(1) remove
O(1) getRandom 을 모두 정확히 이해하고 있느냐에 대한 문제이다.

HashSet은 value가 없는 케이스, value와 같은 케이스 모두를 의미한다. 
'''