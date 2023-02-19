"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.
"""
from typing import List

class Solution:
    def findDuplicate(
        self,
        nums: List[int]
    ) -> int:
        low = 1
        high = len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count <= mid:
                low = mid +1
            else:
                high = mid

        return low 

def main():
    '''
    Run the solution
    '''
    nums = [3,1,3,4,2]
    test = Solution()
    output = test.findDuplicate(nums)
    print(output)

if __name__ == '__main__':
    main()
