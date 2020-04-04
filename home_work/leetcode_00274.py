from typing import List

citations = [3, 0, 6, 1, 5]
citations.sort()
print(citations)
print(citations[-5])


def count_more_then(a, l=[3, 0, 6, 1, 5]):
    n = 0
    for la in l:
        if a >= la:
            n = n + 1
    return n


print(count_more_then(2, l=[3, 0, 6, 1, 5]))


class Solution:

    def hIndex(self, citations: List[int]) -> int:
        citations = citations.sort()
        i = len(citations)
        while i > 0:
            if citations[-i] > i:
                return i
            i = i - 1
        else:
            return 0
