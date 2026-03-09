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
I will create a default dict to store "num" -> "frequency"                                                     - space O(n) storing n elements
Then single loop over the nums array then for every num, I will update or initilize the frequency with += 1    - time O(n) Iterate n elements
Then I will initialize a empty set                                                                             - space O(n) may store upto n elements
Then Until k is greator than 0, look for most frequent in dict                                                 - time O(n) for loop, O(n) value lookup
                                append in set created                                                          - time O(1) avg 
                                remove that from dict                                                          - time O(1) avg

return list(set created)

Time - O(n^2)
Space - O(n)


Optimised Solution:
Step 1: To create frequcncy mapping dict
I will create a default dict to store "num" -> "frequency"                                                     - space O(n) storing n elements
Then single loop over the nums array then for every num, I will update or initilize the frequency with += 1    - time O(n) Iterate n elements

Step 2:
Then I will use bucket mapping method becoz I wanna return the frqucncies and If I search for frequencies from dict then it will take
O(n) and I want k amount of num holding highest frequescies 

So I will create here a array named buckets (list of lists), this will map the index to frequencies and the num to value becoz as
the num can be negative and array cannot have negative frequescies so we use frequescies as index

Then we create a array called result in which we wil store the result we wanna return by looping over buckets from backward, appending
the num in result until len(buckets) == k

return result

Total Complexity:
Time - O(n)
dict, set - lookup, insert remove - O(1)
single loop - O(n)

Space - O(n)  
dict may store upto n elements


Dry Run:
nums = [1, 1, 1, 2, 3], k = 2

Step 1

num = 1
freq[1] = 1

num = 1
freq[1] = 2

num = 1
freq[1] = 3

num = 2
freq[2] = 1

num = 3
freq[3] = 1

Step 2:

buckets = [[] for _ in range len(nums) + 1]
buckets = buckets = [[], [], [], [], [], []]

Step 3:

num = 1
count = 3
buckets[3].append(1)
buckets = [[], [], [], [1], [], []]

num = 2
count = 1
buckets[1].append(2)
buckets = [[], [2], [], [1], [], []]

num = 3
count = 1
buckets[1].append(3)
buckets = [[], [2, 3], [], [1], [], []]

Step 4:

result = []
i = -1
num = empty

result = []
i = -2
num = empty

result = []
i = -3
num = 1
result.append(1)

result = [1]
i = -4
num = empty

result = [1]
i = -5
num = 2
result.append(2)

result = [1, 2]


Code:

from collections import defaultdict

class Solution(object):
    def topKFrequent(self, nums, k):
        
        # step 1
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        # step 2
        buckets = [[] for _ in range(len(nums) + 1)]

        # step 3
        for num, count in freq.items():
            buckets[count].append(num)

        # step 4
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if k == len(result):
                    return result
"""
