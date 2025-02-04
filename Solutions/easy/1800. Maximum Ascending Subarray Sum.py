# Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.
#
# A subarray is defined as a contiguous sequence of numbers in an array.
#
# A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi  < numsi+1. Note that a subarray of size 1 is ascending.
# Example 1:
#
# Input: nums = [10,20,30,5,10,50]
# Output: 65
# Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.
# Example 2:
#
# Input: nums = [10,20,30,40,50]
# Output: 150
# Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.
from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        max_len = 0
        curr_len = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr_len += nums[i]
            else:
                max_len = max(max_len, curr_len)
                curr_len = nums[i]

        return max(max_len, curr_len)
