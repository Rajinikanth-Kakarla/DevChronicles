class Solution:
    def singleNumber(self, nums: List[int]) -> int: #nums = [2,2,3,2]
        """count = 0
        l = len(nums) # 4
        for i in range(l)              # 0      0   0
            for j in range(i+1,l):     # 1 2 3  1 2 1
                if nums[i] == nums[j]: # 1 1 2  0 1 0
                    count+=1
            if count == 2 and count == 1: 
                nums.pop(i)            # pop(0), pop(0) """
        for i in nums:
            if nums.count(i) == 1:   
                a = nums.index(i)
        return nums[a]
    
            

            