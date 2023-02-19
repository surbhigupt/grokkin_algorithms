"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. 

If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always 
considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.
"""

from typing import List

class Solution():

    def find_peak_element(
        self,
        nums: List[int],
    ) -> int:
        
        nums.insert(0, float('-inf'))
        nums.append(float('inf'))

        left, right = 1, len(nums) - 2
        while left <= right:
            mid = (left + right)//2
            if (nums[mid] > nums[mid-1]) and (nums[mid] > nums[mid+1]):
                return nums[mid], mid-1
            elif nums[mid] > nums[mid-1]:
                left = mid + 1
            else:
                right = mid - 1

def main():
    '''
    Run the solution
    '''
    nums = [1,2,1,3,5,6,4]
    test = Solution()
    output = test.find_peak_element(nums)
    print(f'peak number is {output[0]} at index {output[1]}')

if __name__ == '__main__':
    main()
