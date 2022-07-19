"""
Input: nums = [1, 2, 3, 4]
Output: [1, 3, 6, 10]
Explanation: Running sim is obtained as fallows: [1, 1+2, 1+2+3, 1+2+3+4]
"""
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        newlist = []
        temp = 0
        for index, num in enumerate(nums):
            if index > 0:
                temp += num
                newlist.append(temp)
            else:
                temp = num
                newlist.append(temp)

        return newlist


solution = Solution()
solution.runningSum([1, 2, 3, 4])

"""
07/18/2022 13:49
Success
Details 
Runtime: 47 ms, faster than 82.37% of Python3 online submissions for Running Sum of 1d Array.
Memory Usage: 14 MB, less than 71.01% of Python3 online submissions for Running Sum of 1d Array.
"""
