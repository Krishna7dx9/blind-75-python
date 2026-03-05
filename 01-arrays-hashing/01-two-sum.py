"""
Blind 75 — Phase 1: Arrays & Hashing
Problem 1: Two Sum

Description:
Given an array of integers 'nums' and an integer 'target', 
return indices of the two numbers such that they add up to 'target'.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

Return the answer in any order.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9
"""

# -----------------------------
# Brute Force Solution
# -----------------------------
# Approach:
# Check all pairs using two nested loops.
# Time Complexity: O(n^2)
# Space Complexity: O(1)

class TwoSumBruteForce(object):
    def twoSum(self, nums, target):
        for index1 in range(len(nums)):
            for index2 in range(index1 + 1, len(nums)):
                if nums[index1] + nums[index2] == target:
                    return [index1, index2]

# -----------------------------
# Optimized Solution (Hash Map)
# -----------------------------
# Approach:
# Use a hash map to store seen numbers and their indices.
# Check for complement (target - current value) in hash map.
# Time Complexity: O(n)
# Space Complexity: O(n)

class TwoSumOptimized(object):
    def twoSum(self, nums, target):
        seen = {}  # value -> index
        for index, value in enumerate(nums):
            complementary = target - value
            if complementary in seen:
                return [seen[complementary], index]
            seen[value] = index

# -----------------------------
# Example Usage
# -----------------------------
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    # Brute force
    bf_solution = TwoSumBruteForce()
    print("Brute Force Output:", bf_solution.twoSum(nums, target))

    # Optimized
    opt_solution = TwoSumOptimized()
    print("Optimized Output:", opt_solution.twoSum(nums, target))