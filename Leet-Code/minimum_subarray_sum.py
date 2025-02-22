"""class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = [[]]
        temp = []
        for i in range(len(nums)+1):
            for j in range(i):
                l.append(nums[j:i])
        for i in range(len(l)):
            if sum(l[i]) == target:
                temp.append(len(l[i]))
        while len(temp)>0:
            a = sorted(temp)
            return a[0]
            break
        else: 
            return 0
        """

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_len = float('inf')
        curr_sum = 0
        
        for right in range(len(nums)):
            curr_sum += nums[right]
            
            while curr_sum >= target:
                min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1
                
        return min_len if min_len != float('inf') else 0