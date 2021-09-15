#문제:문제: 2d array로 길을 가기 위한 비용이 주어진다. 왼쪽 위에서 오른족 아래까지 도달하기 위한 최소 비용은 얼마인가?

from typing import List


def minPathSum(grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    minCost2d = a = [[0] * cols for i in range(rows)]

    # initialize 2d cost map
    minCost2d[0][0] = grid[0][0]
    for colIdx in range(1, cols):
        minCost2d[0][colIdx] = grid[0][colIdx] + minCost2d[0][colIdx - 1]
    for rowIdx in range(1, rows):
        minCost2d[rowIdx][0] = grid[rowIdx][0] + minCost2d[rowIdx - 1][0]

    # bottom up DP
    for rowIdx in range(1, rows):
        for colIdx in range(1, cols):
            prevCol = colIdx - 1
            prevRow = rowIdx - 1

            upCost = 0 if (prevRow < 0) else minCost2d[prevRow][colIdx]
            leftCost = 0 if (prevCol < 0) else minCost2d[rowIdx][prevCol]

            prevCost = min(upCost, leftCost)
            cost = prevCost + grid[rowIdx][colIdx]
            minCost2d[rowIdx][colIdx] = cost

    minCost = minCost2d[rows - 1][cols - 1]
    return minCost