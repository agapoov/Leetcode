# You are given an array of integers nums. Return the length of the longest subarrayof nums which is either
# strictly increasingor strictly decreasing.

# Example 1:
#
# Input: nums = [1,4,3,3,2]
#
# Output: 2
#
# Explanation:
#
# The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].
#
# The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].
#
# Hence, we return 2.

from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_both = 1
        max_len = 1
        min_len = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                max_len += 1
                min_len = 1
            elif nums[i] < nums[i-1]:
                min_len += 1
                max_len = 1
            else:
                max_len = min_len = 1
            max_both = max(max_both, max_len, min_len)

        return max_both
