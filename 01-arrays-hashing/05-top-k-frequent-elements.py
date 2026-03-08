"""
Thought Process

Input: Given
List of Int : nums
Integer: k 

Output: return
k most frequent element (Order not matters)

Constrains:
1 <= nums.length <= 10^5    - Array can be very large 100000 elements. O(n^2) Algorithm will be too slow. Prefer O(nlogn) or O(n)
-104 <= nums[i] <= 10^4      - Numbers are bounded total values 200001 so Teachniques possible is array, hashmap
k is in the range [1, the number of unique elements in the array]. - We don't need to handle invalid case
It is guaranteed that the answer is unique. - We will never face tie breaking case

Edge case:
nums = [1], k = 1                           minimum input array
nums = [1, 1], k = 1                        all same input
nums = [1,2,3], k = 2                       all different array

Folow-up:
Alorithm Time compllexity must be better than O(nlogn)

Brute Force Solution:
I Did'nt got any unoptimised solution in my mind for this problem as i done group anagraps previous so I found similar approch

Optimised Solution:
I will create a default dict to store "num" -> "frequency"                                                     - space O(n) storing n elements
Then single loop over the nums array then for every num, I will update or initilize the frequency with += 1    - time O(n) Iterate n elements
Then I will initialize a empty set                                                                             - space O(n) may store upto n elements
Then Until k is greator than 0, look for most frequent in dict                                                 - time O(1) avg
                                append in set created                                                          - time O(1) avg 
                                remove that from dict                                                          - time O(1) avg
return list(set created)

Total Complexity:
Time - O(n)     
dict, set -lookup, insert remove - O(1)
single loop - O(n)

Space - O(n^2)  
set, dict may store upto n elements


Dry Run:



Code:






"""
