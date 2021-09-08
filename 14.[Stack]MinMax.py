from typing import List


class MinStack:
    def __init__(self):
        self._stack = []
        self._min_stack = []

    def push(self, val: int) -> None:
        if len(self._stack) == 0:
            self._stack.append(val)
            self._min_stack.append(val)
            return

        min_num = self._min_stack[-1]
        if val < min_num:
            self._stack.append(val)
            self._min_stack.append(val)

        else:
            self._stack.append(val)
            self._min_stack.append(min_num)

    def pop(self) -> None:
        if len(self._stack) != 0:
            self._stack.pop()
            self._min_stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min_stack[-1]

minStack = MinStack()
minStack.push(5)
print(minStack.getMin(),end=' ')
minStack.push(3)
print(minStack.getMin(),end=' ')
minStack.push(2)
print(minStack.getMin(),end=' ')
minStack.push(4)
print(minStack.getMin(),end=' ')
minStack.pop()
minStack.pop()
print(minStack.getMin(),end=' ')