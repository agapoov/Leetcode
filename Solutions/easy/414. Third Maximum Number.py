# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not
# exist, return the maximum number.

# Example 1:
#
# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.
# Example 2:
#
# Input: nums = [1,2]
# Output: 2
# Explanation:
# The first distinct maximum is 2.
# The second distinct maximum is 1.
# The third distinct maximum does not exist, so the maximum (2) is returned instead.

from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first,second,third = float('-inf'), float('-inf'), float('-inf')
        for num in nums:
            if num > first:
                first, second, third = num, first, second
            elif first > num > second:
                second, third = num, second
            elif second > num > third:
                third = num
        return third if third != float('-inf') else first
