"""
49. Group Anagrams
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""


# Brute Force Solution - Compare every pair of strings. If two strings are anagrams, put them in a group.

def groupAnagrams(strs):

    groups = []
    n = len(strs)
    used = [False]*n

    for i in range(n):

        if used[i]:
            continue

        group = [strs[i]]
        used[i] = True

        for j in range(i+1, n):

            if sorted(strs[i]) == sorted(strs[j]):
                group.append(strs[j])
                used[j] = True

        groups.append(group)

    return groups

# Time - O(n² · k log k)
# space - 


# Optimisation Using frequency

from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        # Initialize a default dictionary to hold groups
        groups = defaultdict(list)
        
        # Iterate over each word in the input
        for word in strs:
            # Create a frequency array for 26 lowercase letters
            count = [0] * 26
            for c in word:
                # Increment the count for the corresponding character
                count[ord(c) - ord('a')] += 1
            
            # Use the frequency tuple as a key in the dictionary
            groups[tuple(count)].append(word)
        
        # Return all the grouped anagrams
        return list(groups.values())


# Optimised Solution Using Sorting

from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        groups  = defaultdict(list)
        
        for word in strs:
            key = "".join(sorted(word))
            groups[key].append(word)
        return list(groups.values())


# Optimised Solution using ASCII values

from collections import defaultdict

def groupAnagrams(strs):

    groups = defaultdict(list)
    for word in strs:
        count = [0] * 26
        for c in word:
            count[ord(c) - ord('a')] += 1
        groups[tuple(count)].append(word)
    return list(groups.values())