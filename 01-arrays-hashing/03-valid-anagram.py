"""
242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
"""

# Brute Force Solution

class Solution(object):
    def isAnagram(self, s, t):
        if len(t) != len(s):
            return False

        t_list = list(t)

        for char in s:                             
            if char in t_list:
                t_list.remove(char)
            else:
                return False
        return True

# Time - O(n^2)
# Space - O(n)

# optimised Solution

class Solution(object):
    def isAnagram(self, s, t):
        if len(t) != len(s):
            return False

        freq = {}

        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        for char in t:
            if char in freq:
                freq[char] -=1
                if freq[char] < 0:
                    return False
            else:
                return False
        return True

# TIme - O(n)
# Space - O(n)