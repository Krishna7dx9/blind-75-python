"""
217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true

Explanation:
The element 1 occurs at the indices 0 and 3.
"""

# Brute Force Solution

class Solution(object):
    def containsDuplicate(self, nums):
            for index1 in range(len(nums)):
                for index2 in range(index1 + 1, len(nums)):
                    if nums[index1] == nums[index2]:
                        return True    
            return False

# TIme - O(n^2)
# Space - O(1)


# Optimised Solution

class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for value in nums:
            if value in seen:
                return True 
            seen.add(value)
        return False

# Time - O(n)
# Space - O(n)    