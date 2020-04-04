from typing import List


def findKthLargest(nums: List[int], k: int) -> int:
    k_max = 0
    while k > 0:
        k_max = max(nums)
        print(k_max)
        nums.remove(k_max)
        k = k - 1
    return k_max


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(findKthLargest(nums, k))
    print('=' * 100)
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print(findKthLargest(nums, k))

