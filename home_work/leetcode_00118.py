# 118. 杨辉三角
from utils.dateUtils import run_time

@run_time
class Solution(object):

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if numRows <= 0:
            return []
        if numRows == 1:
            return [[1]]

        bf_gen = self.generate(numRows - 1)

        def f(numRows, x):
            if numRows == x or x == 0 or numRows == 0:
                return 1
            return bf_gen[numRows - 1][x - 1] + bf_gen[numRows - 1][x]

        return bf_gen + [[f(numRows - 1, x) for x in range(numRows)]]


if __name__ == '__main__':
    print([x for x in range(5)])
    # print([f(4, x) for x in range(5)])

    s = Solution()
    for x in s.generate(20):
        print(x)
