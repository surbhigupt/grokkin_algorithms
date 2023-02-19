"""
Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.
"""
from typing import List

class Solution:
    def splitArray(
        self,
        nums: List[int],
        splits: int
    ) -> int:

        low, high = max(nums), sum(nums)
        while low < high:
            mid = (low + high) // 2
            total, count = 0, 1
            for num in nums:
                if total + num <= mid:
                    total += num
                else:
                    total = num
                    count += 1
            if count > splits:
                low = mid + 1
            else:
                high = mid

        return high

def main():
    '''
    Run the solution
    '''
    nums = [7,2,5,10,8]
    k = 2
    test = Solution()
    output = test.splitArray(nums, k)
    print(output)

if __name__ == '__main__':
    main()