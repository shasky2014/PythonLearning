from typing import List

grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
print(grid)
print([max(x) for x in grid])
row_max = [max(x) for x in grid]
grid_t = [[x[i] for x in grid] for i in range(len(grid[0]))]
print(grid_t)
print([max(x) for x in grid_t])
print([max([x[i] for x in grid]) for i in range(len(grid[0]))])
col_max = [max(x) for x in grid_t]
print('-' * 100)

new_grid = [[y for y in x] for x in grid]
print(new_grid)
print(grid)

# print(len(grid))
# print(len(grid[0]))

print('-' * 100)

i = 0
while i < len(grid):
    # print(i)
    j = 0
    while j < len(grid[0]):
        # print(i, j, new_grid[i][j], row_max[i], col_max[j], min(row_max[i], col_max[j]))
        if new_grid[i][j] < min(row_max[i], col_max[j]):
            new_grid[i][j] = min(row_max[i], col_max[j])
        j = j + 1
    i = i + 1

print(new_grid)
print(grid)
print('=' * 100)

print(sum([sum(x) for x in new_grid]) - sum([sum(x) for x in grid]))


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max = [max(x) for x in grid]
        col_max = [max([x[i] for x in grid]) for i in range(len(grid[0]))]
        row_len = len(row_max)
        col_len = len(col_max)

        out_sum = 0
        i = 0
        while i < row_len:
            j = 0
            while j < col_len:
                if grid[i][j] < min(row_max[i], col_max[j]):
                    out_sum += min(row_max[i], col_max[j]) - grid[i][j]
                j = j + 1
            i = i + 1

        return out_sum
